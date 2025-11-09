import os
from opciones import maquina1
from opciones import guardarpuntaje
import time as t

def interfazinicial():
    return """-------------------------------------
\t MAQUINA DE APUESTAS
\t Dev: minervianout
OPCIONES
1. Jugar
2. Ver puntaje total
3. Salir
-------------------------------------"""


error_op = ""
error_op_m1 = str()
os.system("cls")
QuiereSalir = False

puntaje_global_m1 = 0

while True:
    print(interfazinicial())
    print(error_op)
    op_if_inicial = input("Seleccione una opción: ")
    if op_if_inicial.isnumeric():
        op_if_inicial = int(op_if_inicial)
        
        while int(op_if_inicial) in range(1,4): # 1,2,3
            error_op = ""
            
            if op_if_inicial == 1:
                os.system("cls")
                print(error_op_m1)
                tiradas_m1 = input("¿Cuántas veces desea jugar?: ")
                if tiradas_m1.isnumeric():
                    
                    tiradas_m1 = int(tiradas_m1)
                    for i in range(tiradas_m1):
                        os.system("cls")
                        puntaje_global_m1 = maquina1.vismaquina1(puntaje_global_m1)
                    else:
                        os.system("cls")
                        maquina1.finmaquina1(puntaje_global_m1)
                        t.sleep(.5)
                        os.system("cls")
                        puntaje_global_m1 = 0
                        break
                else:
                    error_op_m1 = "La opción no es correcta"
                
            
            if op_if_inicial == 2:
                os.system("cls")
                puntaje = guardarpuntaje.mostrarpuntajem1()
                print(f"Tu puntaje actual es: {puntaje}")
                t.sleep(.5)
                break

            if op_if_inicial == 3:
                os.system("cls")
                QuiereSalir = True
                break
            
        else:
            error_op = "la opción no existe"
            os.system("cls")
            
        if QuiereSalir: break




