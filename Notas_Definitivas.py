from tkinter import *                                            #Importamos toda la libreria Tkinter
import time

ventana = Tk()

ventana.title("Calculo de Notas por MisaVnz-GabrielBaute")      #El comando .title es para agregar un titulo a nuestra ventana
ventana.geometry("800x600")                                     #El comando .geometry es para agregar la resolucion de la ventana inicial

texto1 = Label(ventana, text=("Bienvenidos a Notedef-Unefa V0.1"))
texto1.pack()



print("Corte Uno: Introduce tus notas")    #Aplicacion creada por Misael para sacar el calculo de las notas definitivas V0.1
pcor1 = float(input("Primera prueba corta:"))  #pcor son las variables para las pruebas cortas
result_pc1 = (pcor1 * 0.05)                    #Las pruebas cortas se multiplican por el 5% que es la valoracion dada por la Unefa para las pruebas cortas
pcor2 = float(input("Segunda prueba corta:"))  #Por corte segun el reglamento de la UNEFA son dos pruebas cortas y una prueba parcial
result_pc2 = (pcor2 * 0.05)
pp1 =  float(input("Primer parcial:"))
result_pp1 = (pp1 * 0.15)                      #Las pruebas parciales tienen una ponderacion del 15% en el reglamento
suma1 = (result_pc1+result_pc2+result_pp1)
print(f"La nota del primer corte es {suma1}")
print("Corte Dos: Introduce tus notas")    
pcor3 = float(input("Primera prueba corta:"))  
result_pc3 = (pcor3 * 0.05)                    
pcor4 = float(input("Segunda prueba corta:"))  
result_pc4 = (pcor4 * 0.05)
pp2 =  float(input("Primer parcial:"))
result_pp2 = (pp2 * 0.15)                      
suma2 = (result_pc3+result_pc4+result_pp2)
print(f"La nota del segundo corte es {suma2}")
print("Corte Tres: Introduce tus notas")    
pcor5 = float(input("Primera prueba corta:"))  
result_pc5 = (pcor5 * 0.05)                    
pcor6 = float(input("Segunda prueba corta:"))  
result_pc6 = (pcor6 * 0.05)
pp3 =  float(input("Primer parcial:"))
result_pp3 = (pp3 * 0.15)                      
suma3 = (result_pc5+result_pc6+result_pp3)
print(f"La nota del cuarto corte es {suma3}")
print("Corte Cuatro: Introduce tus notas")    
pcor7 = float(input("Primera prueba corta:"))  
result_pc7 = (pcor7 * 0.05)                    
pcor8 = float(input("Segunda prueba corta:"))  
result_pc8 = (pcor8 * 0.05)
pp4 =  float(input("Primer parcial:"))
result_pp4 = (pp4 * 0.15)                      
suma4 = (result_pc7+result_pc8+result_pp4)
print(f"La nota del cuarto corte es {suma4}")
notadef = (suma1+suma2+suma3+suma4)
print(f"La nota definitiva de esta materia es: {notadef}")
