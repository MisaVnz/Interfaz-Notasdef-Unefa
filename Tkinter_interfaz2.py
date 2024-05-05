from tkinter import *
import time

ventana =Tk()

ventana.title("Calculo de Notas por MisaVnz-GabrielBaute")
ventana.geometry("700x300")


texto1= Label(ventana, text="Bienvenidos a Notedef-Unefa V0.1",font="Curier 15")
texto1.place(x=210, y=13)

texto2= Label(ventana, text="Primera prueba corta: ", font="Curier 10")
texto2.place(x=60, y=60)

texto3= Label(ventana, text="Segunda prueba corta: ", font="Curier 10")
texto3.place(x=60, y=100)

texto4= Label(ventana, text="Prueba parcial:", font="Curier 10" )
texto4.place(x=80, y=140)

textoC= Label(ventana, text="Nota del corte: ", font="Curier 10")
textoC.place(x=80, y=180)

texto5= Label(ventana, text="Corte 1: ", font="Curier 10")
texto5.place(x=400, y=60)

texto6= Label(ventana, text="Corte 2: ", font="Curier 10")
texto6.place(x=400, y=100)

texto7= Label(ventana, text="Corte 3: ",font="Curier 10")
texto7.place(x=400, y=140)

texto8= Label(ventana, text="Corte 4: ",font="Curier 10" )
texto8.place(x=400, y=180)

textoD= Label(ventana, text="Nota Definitiva: ",font="Curier 10")
textoD.place(x=200, y=240)

entrada1= Entry(ventana)
entrada1.place(x=200, y=140)

entrada2= Entry(ventana)
entrada2.place(x=200, y=100)

entrada3= Entry(ventana)
entrada3.place(x=200, y=60)

entrada4= Entry(ventana)
entrada4.place(x=460, y=60)

entrada5= Entry(ventana)
entrada5.place(x=460, y=100)

entrada6= Entry(ventana)
entrada6.place(x=460, y=140)

entrada7= Entry(ventana)
entrada7.place(x=460, y=180)

entrada8= Entry(ventana)
entrada8.place(x=200, y=180)

entrada9= Entry(ventana)
entrada9.place(x=300, y=240)






ventana.mainloop()
