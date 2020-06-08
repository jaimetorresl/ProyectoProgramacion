# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy.integrate as inte

# Definimos la función F1
def F1(y1,y2,Trr):
    alpha = 1 - np.sqrt(y1**2 + y2**2)
    return alpha * y1 - ((2.0*np.pi)/Trr)*y2

# Definimos la función F2
def F2(y1, y2, Trr):
    alpha = 1 - np.sqrt(y1**2 + y2**2)
    return alpha * y2 + ((2.0*np.pi)/Trr)*y1

def F3(y1,y2,y3,a,b,ti,tMuestreo):
    theta = np.arctan2(y1,y2)
    suma = 0
    for i in range(5):
        dthetai = np.fmod(theta - ti[i], 2 * np.pi)*-1
        suma += (a[i]*dthetai*np.exp(-(dthetai**2/(2*(b[i]**2)))))
    z0 =  (1.5 * 10**(-4)) * np.sin(2 * np.pi * 0.25 * (tMuestreo))
    return suma*-1 - (y3-z0)



def EulerForward(y1,y2,y3, FrecuenciaCardiaca = 60, NumLatidos = 10, FrecuenciaMuestreo = 360, a=[1.2,-5.0,30.0,-7.5,0.75], b=[0.25,0.1,0.1,0.1,0.4],ti=[(-1/3)*np.pi,(-1/12)*np.pi,0,(1/12)*np.pi, (1/2)*np.pi]):
    #Defininimos el avance
    h = 1 / FrecuenciaMuestreo
    # Definimos la condición inicial para Y1 y Y2
    Y10 = y1
    Y20 = y2
    Y30 = y3
    # Definimos el tiempo inicial
    To = 0.0
    # Definimos el tiempo final
    Tf = NumLatidos

    meanFc = 60 / FrecuenciaCardiaca


    # Creamos un arreglo de tiempo que vaya
    # desde To hasta Tf con pasos de h
    T = np.arange(To, Tf + h, h)
    # RR para calcular el omega, es el componente aleatorio de W(omega)
    tRR = np.random.normal(meanFc, meanFc * 0.05, np.size(T))

    # Definimos un arreglo para ir almacenando
    # los valores estimados de Y1(t) en cada iteración
    Y1EulerFor = np.zeros(len(T))
    Y2EulerFor = np.zeros(len(T))
    Y3EulerFor = np.zeros(len(T))

    Y1EulerFor[0] = Y10
    Y2EulerFor[0] = Y20
    Y3EulerFor[0] = Y30

    for iter in range(1, len(T)):
        Y1EulerFor[iter] =  Y1EulerFor[iter-1] + h * F1(Y1EulerFor[iter-1],Y2EulerFor[iter-1],tRR[iter] )
        Y2EulerFor[iter] = Y2EulerFor[iter-1] +h * F2(Y1EulerFor[iter-1],Y2EulerFor[iter-1], tRR[iter])
        Y3EulerFor[iter] = Y3EulerFor[iter-1] + h * F3(Y1EulerFor[iter-1],Y2EulerFor[iter-1],Y3EulerFor[iter-1],a,b,ti,FrecuenciaMuestreo)
    return T,Y3EulerFor


def EulerBack(y1,y2,y3, FrecuenciaCardiaca = 60, NumLatidos = 10, FrecuenciaMuestreo = 360, a=[1.2,-5.0,30.0,-7.5,0.75], b=[0.25,0.1,0.1,0.1,0.4],ti=[(-1/3)*np.pi,(-1/12)*np.pi,0,(1/12)*np.pi, (1/2)*np.pi]):
    #Defininimos el avance
    h = 1 / FrecuenciaMuestreo
    # Definimos la condición inicial para Y1 y Y2
    Y10 = y1
    Y20 = y2
    Y30 = y3
    # Definimos el tiempo inicial
    To = 0.0
    # Definimos el tiempo final
    Tf = NumLatidos

    meanFc = 60 / FrecuenciaCardiaca

    # RR para calcular el omega
    # Creamos un arreglo de tiempo que vaya
    # desde To hasta Tf con pasos de h
    T = np.arange(To, Tf + h, h)
    tRR = np.random.normal(meanFc, meanFc * 0.05, np.size(T))

    # Definimos un arreglo para ir almacenando
    # los valores estimados de Y1(t) en cada iteración
    Y1EulerBack = np.zeros(len(T))
    Y2EulerBack = np.zeros(len(T))
    Y3EulerBack = np.zeros(len(T))

    Y1EulerBack[0] = Y10
    Y2EulerBack[0] = Y20
    Y3EulerBack[0] = Y30

    for iter in range(1, len(T)):
        Y1EulerBack[iter] =  Y1EulerBack[iter-1] + h * F1(Y1EulerBack[iter-1],Y2EulerBack[iter-1],tRR[iter-1] )
        Y2EulerBack[iter] = Y2EulerBack[iter-1] + h * F2(Y1EulerBack[iter-1],Y2EulerBack[iter-1], tRR[iter-1])
        Y3EulerBack[iter] = Y3EulerBack[iter-1] + h * F3(Y1EulerBack[iter],Y2EulerBack[iter],Y3EulerBack[iter],a,b,ti,FrecuenciaMuestreo)
    return T,Y3EulerBack

def EulerMod(y1,y2,y3, FrecuenciaCardiaca = 60, NumLatidos = 10, FrecuenciaMuestreo = 360, a=[1.2,-5.0,30.0,-7.5,0.75], b=[0.25,0.1,0.1,0.1,0.4],ti=[(-1/3)*np.pi,(-1/12)*np.pi,0,(1/12)*np.pi, (1/2)*np.pi]):
    #Defininimos el avance
    h = 1 / FrecuenciaMuestreo
    # Definimos la condición inicial para Y1 y Y2
    Y10 = y1
    Y20 = y2
    Y30 = y3
    # Definimos el tiempo inicial
    To = 0.0
    # Definimos el tiempo final
    Tf = NumLatidos

    meanFc = 60 / FrecuenciaCardiaca

    # RR para calcular el omega
    # Creamos un arreglo de tiempo que vaya
    # desde To hasta Tf con pasos de h
    T = np.arange(To, Tf + h, h)

    tRR = np.random.normal(meanFc, meanFc * 0.05, np.size(T))

    # Definimos un arreglo para ir almacenando
    # los valores estimados de Y1(t) en cada iteración
    Y1EulerMod = np.zeros(len(T))
    Y2EulerMod = np.zeros(len(T))
    Y3EulerMod = np.zeros(len(T))

    Y1EulerMod[0] = Y10
    Y2EulerMod[0] = Y20
    Y3EulerMod[0] = Y30

    for iter in range(1, len(T)):
        Y1EulerMod[iter] =  Y1EulerMod[iter-1] + (h/2.0) * (F1(Y1EulerMod[iter-1],Y2EulerMod[iter-1],tRR[iter]) + F1(Y1EulerMod[iter],Y2EulerMod[iter],tRR[iter]))
        Y2EulerMod[iter] = Y2EulerMod[iter-1] +(h/2.0) *  (F2(Y1EulerMod[iter-1],Y2EulerMod[iter-1],tRR[iter]) + F2(Y1EulerMod[iter],Y2EulerMod[iter], tRR[iter]))
        Y3EulerMod[iter] = Y3EulerMod[iter-1] + (h/2.0) *   (F3(Y1EulerMod[iter-1],Y2EulerMod[iter-1],Y3EulerMod[iter-1],a,b,ti,FrecuenciaMuestreo)+  F3(Y1EulerMod[iter],Y2EulerMod[iter],Y3EulerMod[iter],a,b,ti,FrecuenciaMuestreo))
    return T,Y3EulerMod

