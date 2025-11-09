import numpy as np
import time as t
from opciones import guardarpuntaje

def logmaquina1():
    punt_tirada = int()
    xo = np.array(["o","x"])
    array = np.random.choice(xo, size=(4, 4)).astype('<U4')
        
    pos = ["o","Ho"]
    l0 = str()
    l1 = str()
    l2 = str()
    l3 = str()
                
    for f in range(array.shape[0]):
        if all(array[f,:] == "o"):
            array[f,:] = "Ho"
            punt_tirada += 100

    for c in range(array.shape[1]):
        if all(x in pos for x in array[:, c]):
            array[array[:,c] =="Ho", c] = "HVo"
            array[array[:,c] == "o", c] = "Vo"
            
            if any(array[:,c] == "Vo"):
                punt_tirada += 100
            
            if any(array[:,c] == "HVo"):
                punt_tirada += 200
            
    for f in range(array.shape[0]):
        for c in range(array.shape[1]):
            if array[f,c] == "x":
                if f == 0:
                    l0 += f"\033[1;30m x \033[0m"
                if f == 1:
                    l1 += f"\033[1;30m x \033[0m"
                if f == 2:
                    l2 += f"\033[1;30m x \033[0m"
                if f == 3:
                    l3 += f"\033[1;30m x \033[0m"
                    
            if array[f,c] == "o":
                if f == 0:
                    l0 += f"\033[1;30m o \033[0m"
                if f == 1:
                    l1 += f"\033[1;30m o \033[0m"
                if f == 2:
                    l2 += f"\033[1;30m o \033[0m"
                if f == 3:
                    l3 += f"\033[1;30m o \033[0m"
            
            if  array[f,c] == "Ho":
                if f == 0:
                    l0 += f"\033[1;32m o \033[0m"
                if f == 1:
                    l1 += f"\033[1;32m o \033[0m"
                if f == 2:
                    l2 += f"\033[1;32m o \033[0m"
                if f == 3:
                    l3 += f"\033[1;32m o \033[0m"
            
            if array[f,c] == "HVo":
                if f == 0:
                    l0 += f"\033[1;33m o \033[0m"
                if f == 1:
                    l1 += f"\033[1;33m o \033[0m"
                if f == 2:
                    l2 += f"\033[1;33m o \033[0m"
                if f == 3:
                    l3 += f"\033[1;33m o \033[0m"
            
            if array[f,c] == "Vo":
                if f == 0:
                    l0 += f"\033[1;32m o \033[0m"
                if f == 1:
                    l1 += f"\033[1;32m o \033[0m"
                if f == 2:
                    l2 += f"\033[1;32m o \033[0m"
                if f == 3:
                    l3 += f"\033[1;32m o \033[0m"
        
    else:
        return l0,l1,l2,l3,punt_tirada

def vismaquina1(puntaje_global):
    l0,l1,l2,l3,punt_tirada = logmaquina1()
    punt_tirada = puntaje_global + punt_tirada
    
    print(f"""-----------------------------------
\t MAQUINA INICIADA""")
    t.sleep(.5)
    print(f"\t   {l0}")
    t.sleep(.5)
    print(f"\t   {l1}")
    t.sleep(.5)
    print(f"\t   {l2}")
    t.sleep(.5)
    print(f"\t   {l3}")
    t.sleep(.5)
    print(f"Tu puntaje actual es: {punt_tirada}")
    print("-----------------------------------")
    t.sleep(1)
    return punt_tirada

def finmaquina1(puntaje_global):
   t.sleep(.5)
   print(
"""-------------------------------
Guardando puntaje en la cuenta...
-------------------------------""")
   guardarpuntaje.guardarpuntajem1(puntaje_global)
   t.sleep(2)
   print(
"""------------------------------
¡Puntaje guardado con éxito!
------------------------------""")

