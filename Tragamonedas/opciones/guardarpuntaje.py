import pandas as pd

def guardarpuntajem1(puntaje_global):
    df = pd.read_csv("csv\\puntaje.csv")
    df.iloc[0,0] = df.iloc[0,0].astype(int) + puntaje_global 
    df.to_csv("csv\\puntaje.csv", index=False)
    
def mostrarpuntajem1():
    df = pd.read_csv("csv\\puntaje.csv")
    puntaje = df.iloc[0,0].astype(int)
    return(puntaje)