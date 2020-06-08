
import tkinter as tk
import  PIL
from PIL import Image
from PIL import ImageTk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from ECG import EulerForward
import matplotlib.pyplot as plt
import numpy as np

'''Configuramos la Ventana'''
window = tk.Tk()  # Definimos la ventana con nombre window
window.geometry('1080x720')  # Tamaño de la ventana
window.title('Diferentes funciones - Programación Científica')
window.config(cursor="arrow")
# tipo de cursor: "arrow","circle","clock","cross",
# "dotbox","exchange","fleur","heart","man","mouse",
# "pirate","plus","shuttle","sizing","spider","spraycan",
# "star","target","tcross","trek","watch"

'''Definimos los Frames y sus configuraciones para organizar la GUI'''
frame1 = tk.Frame(master=window)
frame1.place(x=0, y=0)
frame1.config(bg="#2F3E46", width=1080, height=720, bd=8)

'''Se definen todas las funciones requeridas'''
def CerrarAplicacion():
    MsgBox = tk.messagebox.askquestion ('Cerrar Aplicación','¿Está seguro que desea cerrar la aplicación?',icon = 'warning')
    if MsgBox == 'yes':
       window.destroy()
    else:
        tk.messagebox.showinfo('Retornar','Será retornado a la aplicación')
Boton2 = tk.Button(master=window, text="X", command = CerrarAplicacion, bg='#e63946', fg='#FFF', font='bold',highlightthickness = 0,borderwidth=0).place(x=1044,y=0)

def grafica():
    plt.style.use('seaborn-darkgrid')
    fig = plt.Figure(figsize=(4.55, 3), dpi=100)
    #Si sabe como sacar los datos metalos en el EulerForward prro y mete el "y"
    data = EulerForward(0.025,0,0.006)
    t = data[0]
    y = data[1]
    fig.add_subplot(111).plot(t, y)     # subplot(filas, columnas, item)
    if opcion.get() == 1:
        fig.suptitle("Euler Forward")
    elif opcion.get() == 2:
        fig.suptitle("Euler Backward")
    elif opcion.get() == 3:
        fig.suptitle("Euler Modificando")
    elif opcion.get() == 4:
        fig.suptitle("RK2")
    elif opcion.get() == 5:
        fig.suptitle("RK4")

    plt.close()
    Plot = FigureCanvasTkAgg(fig, master=window)
    Plot.draw()
    Plot.get_tk_widget().place(x=70,y=106)
def exportarDatos():
    x=3

BotonExportar = tk.Button(master=frame1, text="Exportar datos", command = exportarDatos, width = 10, bg='#354F52', fg='#FFF', font='bold').place(x=150, y=5)
BotonImportar = tk.Button(master=frame1, text="Importar datos", command = exportarDatos, width = 10, bg='#354F52', fg='#FFF', font='bold').place(x=300, y=5)

titulo = tk.Label(master=frame1, bg="#354F52",fg='#FFF', font=('Arial', 15, 'bold'), text=f"señal de ECG",width=41).place(x=62,y=70)

def HR():
    y = 5
    resul.set(y)

BotonHR = tk.Button(master=frame1, text="Hallar HR", command = exportarDatos, width = 10, bg='#354F52', fg='#FFF', font='bold').place(x=150, y=430)

resul = tk.StringVar()
HR()
lbHRresp = tk.Label(master=frame1, textvariable = resul, width = 10, bg='#FFF', font='bold').place(x=300, y=435)
lbParametrosfondo = tk.Label(master=frame1, width = 45, bg='#52796F', font='bold',height=8).place(x=62, y=485)
lbParametros = tk.Label(master=frame1, text = "   \tP\tQ\tR\tS\tT", width = 45, bg='#354F52',fg='#FFF', font='bold').place(x=62, y=485)
lbai = tk.Label(master=frame1, text = "ai", width = 2, bg='#52796F',fg='#FFF', font='bold').place(x=95, y=535)
lbbi = tk.Label(master=frame1, text = "bi", width = 2, bg='#52796F',fg='#FFF', font='bold').place(x=95, y=585)

aiP = tk.StringVar()
entryaiP = tk.Entry(master=frame1, textvariable = aiP, width = 2, bg='#FFF', font='bold').place(x=155, y=535)

aiQ = tk.StringVar()
entryaiQ = tk.Entry(master=frame1, textvariable = aiQ, width = 2, bg='#FFF', font='bold').place(x=235, y=535)

aiR = tk.StringVar()
entryaiR = tk.Entry(master=frame1, textvariable = aiR, width = 2, bg='#FFF', font='bold').place(x=315, y=535)

aiS = tk.StringVar()
entryaiS = tk.Entry(master=frame1, textvariable = aiS, width = 2, bg='#FFF', font='bold').place(x=395, y=535)

aiT = tk.StringVar()
entryaiT = tk.Entry(master=frame1, textvariable = aiT, width = 2, bg='#FFF', font='bold').place(x=475, y=535)



biP = tk.StringVar()
entrybiP = tk.Entry(master=frame1, textvariable = biP, width = 2, bg='#FFF', font='bold').place(x=155, y=585)

biQ = tk.StringVar()
entrybiQ = tk.Entry(master=frame1, textvariable = biQ, width = 2, bg='#FFF', font='bold').place(x=235, y=585)

biR = tk.StringVar()
entrybiR = tk.Entry(master=frame1, textvariable = biR, width = 2, bg='#FFF', font='bold').place(x=315, y=585)

biS = tk.StringVar()
entrybiS = tk.Entry(master=frame1, textvariable = biS, width = 2, bg='#FFF', font='bold').place(x=395, y=585)

biT = tk.StringVar()
entrybiT = tk.Entry(master=frame1, textvariable = biT, width = 2, bg='#FFF', font='bold').place(x=475, y=585)



fondoParametros = tk.Label(master=frame1,bg="#52796F", width=41, font=('Arial', 15, 'bold'), height=13 ).place(x=575, y=82)
parametrosTitulo = tk.Label(master=frame1, bg="#354F52",fg='#FFF', font=('Arial', 15, 'bold'), text="Parametros",width=41).place(x=575,y=70)

lbFrecuenciaCardiaca = tk.Label(master=frame1, bg="#52796F",fg='#FFF', font=('Arial', 13, 'bold'), text="Frecuencia cardiaca",width=18).place(x=590,y=132)
frecuenciaCardiaca = tk.StringVar()
entryFrecuenciaCardiaca = tk.Entry(master=frame1, textvariable = frecuenciaCardiaca, width = 15, bg='#FFF', font='bold').place(x=850, y=132)

lbNumeroLatidos = tk.Label(master=frame1, bg="#52796F",fg='#FFF', font=('Arial', 13, 'bold'), text="Número de latidos",width=18).place(x=580,y=202)
numeroLatidos = tk.StringVar()
entryNumeroLatidos = tk.Entry(master=frame1, textvariable = numeroLatidos, width = 15, bg='#FFF', font='bold').place(x=850, y=202)

lbFrecuenciaMuestreo = tk.Label(master=frame1, bg="#52796F",fg='#FFF', font=('Arial', 13, 'bold'), text="Frecuencia muestreo",width=18).place(x=592,y=272)
frecuenciaMuestreo = tk.StringVar()
entryfrecuenciaMuestreo = tk.Entry(master=frame1, textvariable = frecuenciaMuestreo, width = 15, bg='#FFF', font='bold').place(x=850, y=272)

lbFactorRuido = tk.Label(master=frame1, bg="#52796F",fg='#FFF', font=('Arial', 13, 'bold'), text="Factor de ruido",width=15).place(x=582,y=342)
factorRuido = tk.StringVar()
entryfactorRuido = tk.Entry(master=frame1, textvariable = factorRuido, width = 15, bg='#FFF', font='bold').place(x=850, y=342)



img3=Image.open("salud.jpg")
img3= img3.resize((166, 190))
img3 = ImageTk.PhotoImage(img3)
lab3 = tk.Label(image=img3,borderwidth=0)
lab3.place(x=570, y=480)

def hola():
    valor = opcion.get()
    if valor == 1:
        grafica()




fondoParametros = tk.Label(master=frame1,bg="#52796F", width=23, font=('Arial', 15, 'bold'), height=10 ).place(x=760, y=442)
metodoSolucionTitulo = tk.Label(master=frame1, bg="#354F52",fg='#FFF', font=('Arial', 15, 'bold'), text="Método de solucion ED",width=23).place(x=760,y=430)
opcion = tk.IntVar()
Nombre = tk.StringVar()

seno = tk.Radiobutton(master=frame1, text='Euler adelante', value=1, command=hola, variable=opcion, bg='#52796F',fg='#FFF' ,font=('Arial', 13, 'bold'),  highlightthickness = 0, selectcolor='#52796F')
seno.place(x=800,y=475)

coseno = tk.Radiobutton(master=frame1, text='Euler atras', value=2, command=hola, variable=opcion, bg='#52796F',fg='#FFF',font=('Arial', 13, 'bold'),  highlightthickness = 0, selectcolor='#52796F')
coseno.place(x=800,y=515)

exp = tk.Radiobutton(master=frame1, text='Euler modificado', value=3, command=hola, variable=opcion, bg='#52796F',fg='#FFF',font=('Arial', 13, 'bold'),  highlightthickness = 0, selectcolor='#52796F')
exp.place(x=800,y=555)

log = tk.Radiobutton(master=frame1, text='Runge-Kutta 2', value=4, command=hola, variable=opcion, bg='#52796F',fg='#FFF',font=('Arial', 13, 'bold'),  highlightthickness = 0, selectcolor='#52796F')
log.place(x=800,y=595)

sqrt = tk.Radiobutton(master=frame1, text='Runge-Kutta 4', value=5, command=hola, variable=opcion, bg='#52796F',fg='#FFF',font=('Arial', 13, 'bold'),  highlightthickness = 0, selectcolor='#52796F')
sqrt.place(x=800,y=635)
seno.select()

window.mainloop()