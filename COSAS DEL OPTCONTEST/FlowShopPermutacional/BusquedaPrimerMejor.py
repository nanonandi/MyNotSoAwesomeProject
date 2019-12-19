import numpy as np
import funcionF as f
import Evaluar as ev
import GenerarVecinos as vec

def primerMejor (tam,matriz):
    solucion = [0]*tam
    mejor =  [0]*tam
    actual =  [0]*tam
    t_mejor = 1000
    actual = range(tam)
    actual = np.random.permutation(actual)
    mejor = actual
    for i in range (0,len(actual)-1):
        for j in range (0,len(actual)-1):
            if j is not i:
                temp = actual[i]
                actual[i]=actual[j]
                actual[j]=temp
                t_actual = ev.evaluar (f.funcionF(actual,matriz),actual)
                if t_actual < t_mejor:
                    t_mejor = t_actual
                    mejor = actual
    solucion = mejor
    return solucion,t_mejor    
