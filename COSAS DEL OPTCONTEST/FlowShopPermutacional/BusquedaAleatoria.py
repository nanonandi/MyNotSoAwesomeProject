import numpy as np
import funcionF as f
import Evaluar as ev

def busquedaAleatoria(tam,matriz):
    solucion = [0]*tam
    mejor =  [0]*tam
    actual =  [0]*tam
    t_mejor = 0

    actual = range(tam)
    actual = np.random.permutation(actual)
    mejor = actual
    for i in range (200):
        actual = np.random.permutation(actual)
        t_actual = ev.evaluar (f.funcionF(actual,matriz),actual)
        if i == 0:
            mejor = actual
            t_mejor = t_actual
        elif t_actual < t_mejor:
            t_mejor = t_actual
            mejor = actual    
   
    solucion = mejor
    return solucion,t_mejor    
