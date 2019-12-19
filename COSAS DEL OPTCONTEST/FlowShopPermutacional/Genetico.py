import numpy as np
import funcionF as f
import Evaluar as ev
import GenerarVecinos as vec

def genetico(tam,matriz):
    '''
    No realizado
    '''

    solucion = [0]*tam
    mejor =  [0]*tam
    t_mejor = 0
    actual =  [0]*tam


    actual = range(tam)
    actual = np.random.permutation(actual)
    mejor = actual

    poblacion = []
    for i in range (100): #individuos
        actual = range(tam)
        actual = np.random.permutation(actual)
        poblacion.append(actual)


    for i in range (200): #Generaciones

        sele = []
        padres = []
        for x in poblacion:
            if len(sele) < 3:
                sele.append(x)
            else:
                padres.append(selTourThree(sele[0], sele[1], sele[2], matriz))
                sele.clear()
        
        sele.clear()
        hijos = []
        for x in padres:
            if len(sele) < 2:
                sele.append(x)
            else:
                a,b = cxOnePoint(sele[0], sele[1])
                hijos.append(a)
                hijos.append(b)
                sele.clear()

        poblacion.clear()
        poblacion = padres + hijos

        a = random.randint(0,10)

        if(a <= 2):
            b = (random.randint(0,len(poblacion)-1)
            poblacion[b] = mutShuffleIndexes(poblacion[b])
    
    
    for act in range (len(poblacion)-1): #individuos
        if (ev.evaluar(f.funcionF(act,matriz),act) < mejor):
            mejor = act
        

    solucion = mejor
    t_mejor = ev.evaluar(f.funcionF(mejor,matriz),mejor)
    return solucion,t_mejor  




def selTourThree(ind,ivi,duo, matriz):
    
    t_ind = ev.evaluar(f.funcionF(ind,matriz),ind)
    t_ivi = ev.evaluar (f.funcionF(ivi,matriz),ivi)
    t_duo = ev.evaluar (f.funcionF(duo,matriz),duo)
    
    min = np.min([t_ind, t_ivi, t_duo])

    if(t_ind == min):
        return ind
    elif(t_ivi==min):
        return ivi
    elif(t_duo==min):
        return duo


    
def cxOnePoint(indi, viduo):

    """Executes a one point crossover on the input :term:`sequence` individuals.

    The two individuals are modified in place. The resulting individuals will

    respectively have the length of the other.



    :param ind1: The first individual participating in the crossover.

    :param ind2: The second individual participating in the crossover.

    :returns: A tuple of two individuals.



    This function uses the :func:`~random.randint` function from the

    python base :mod:`random` module.

    """

    size = min(len(ind1), len(ind2))

    cxpoint = random.randint(1, size - 1)

    ind1[cxpoint:], ind2[cxpoint:] = ind2[cxpoint:], ind1[cxpoint:]

    return indi, viduo


def mutShuffleIndexes(individuo):
    ran = random.randint(0,len(individuo)-1)
    ren = random.randint(0,len(individuo)-1)

    aux = individuo[ran]

    individuo[ran] = individuo[ren]

    individuo[ren] = aux

    return individuo