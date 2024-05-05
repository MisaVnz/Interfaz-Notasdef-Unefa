from tkinter import *                                            #Importamos toda la libreria Tkinter
import time

ventana = Tk()                                                  #Creamos la variable para la ventana

ventana.title("Calculo de Notas por MisaVnz-GabrielBaute")      #El comando .title es para agregar un titulo a nuestra ventana
ventana.geometry("800x600")                                     #El comando .geometry es para agregar la resolucion de la ventana inicial

def saludo():
    print("Hola te saludo")



texto = Label(ventana, text="Bienvenidos a Notedef-Unefa V0.1") #Agregamos un label mas el texto que queremos mostrar
texto.grid(row=0, column=0)                                                    #Agregamos el .pack() que nos dira en que posicion de nuestra ventana se mostrara el texto
 
boton1 = Button(ventana, text="Has click aca para saludarte", command=saludo)
boton1.place(x=330, y=300)






ventana.mainloop()                                              #Aplicamos el .mainloop() para que nuestra ventana se quede abierta
