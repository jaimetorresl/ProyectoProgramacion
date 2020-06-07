
import tkinter as tk
from PIL import ImageTk ,Image

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


def exportarDatos():
    x=3

BotonExportar = tk.Button(master=frame1, text="Exportar datos", command = exportarDatos, width = 10, bg='#354F52', fg='#FFF', font='bold').place(x=150, y=5)
BotonImportar = tk.Button(master=frame1, text="Importar datos", command = exportarDatos, width = 10, bg='#354F52', fg='#FFF', font='bold').place(x=300, y=5)

titulo = tk.Label(master=frame1, bg="#354F52",fg='#FFF', font=('Arial', 15, 'bold'), text=f"señal de ECG",width=41).place(x=62,y=70)

grafica = tk.Frame(master=window)
grafica.place(x=71, y=106)
grafica.config(bg="#FFF", width=453, height=300, bd=8)

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

fondoParametros = tk.Label(master=frame1,bg="#52796F", width=23, font=('Arial', 15, 'bold'), height=10 ).place(x=660, y=442)
metodoSolucionTitulo = tk.Label(master=frame1, bg="#354F52",fg='#FFF', font=('Arial', 15, 'bold'), text="Método de solucion ED",width=23).place(x=660,y=430)
opcion = tk.IntVar()
Nombre = tk.StringVar()
seno = tk.Radiobutton(master=frame1, text='Euler adelante', value=1, command=grafica, variable=opcion, bg='#52796F',fg='#FFF' ,font=('Arial', 13, 'bold')).place(x=700,y=475)
coseno = tk.Radiobutton(master=frame1, text='Euler atras', value=2, command=grafica, variable=opcion, bg='#52796F',fg='#FFF',font=('Arial', 13, 'bold')).place(x=700,y=515)
exp = tk.Radiobutton(master=frame1, text='Euler modificado', value=3, command=grafica, variable=opcion, bg='#52796F',fg='#FFF',font=('Arial', 13, 'bold')).place(x=700,y=555)
log = tk.Radiobutton(master=frame1, text='Runge-Kutta 2', value=4, command=grafica, variable=opcion, bg='#52796F',fg='#FFF',font=('Arial', 13, 'bold')).place(x=700,y=595)
sqrt = tk.Radiobutton(master=frame1, text='Runge-Kutta 4', value=5, command=grafica, variable=opcion, bg='#52796F',fg='#FFF',font=('Arial', 13, 'bold')).place(x=700,y=635)

window.mainloop()
