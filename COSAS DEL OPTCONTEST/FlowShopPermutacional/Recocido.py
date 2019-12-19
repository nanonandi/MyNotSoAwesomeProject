import numpy as np
import funcionF as f
import Evaluar as ev
import GenerarVecinos as vec

def recocido(tam,matriz):
    t_min = 0.2
    t = 100
    alfa = 0.85
    actual = range(tam)
    actual = np.random.permutation(actual)
    mejor = actual
    t_mejor = ev.evaluar (f.funcionF(actual,matriz),actual)
    while t > t_min:
        for i in range (1,len(actual)):
            t_actual = ev.evaluar (f.funcionF(actual,matriz),actual)
            candidato = np.random.permutation(actual)
            t_candidato = ev.evaluar (f.funcionF(candidato,matriz),candidato)
            delta = t_candidato -t_actual
            aleatorio = np.random.rand()
            if (aleatorio < np.e**((-delta)/t)) or (delta < 0):
                actual = candidato
            t_actual = ev.evaluar (f.funcionF(actual,matriz),actual)
            if t_actual < t_mejor:
                mejor = actual
                t_mejor = t_actual    
        t = alfa*t        
    solucion = mejor
    return solucion,t_mejor