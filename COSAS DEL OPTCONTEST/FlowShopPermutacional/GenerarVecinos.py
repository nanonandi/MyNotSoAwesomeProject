import numpy as np

def generarVecinosAleatorios (solucion):
    nuevasol = np.random.permutation (solucion)
    
    return nuevasol


def generarVecinosDeterminista (solucion):
    temp = 0
    for x in solucion:
        for y in reversed(solucion):
            
            x = temp
            x = y 
            y = temp
            return solucion 


def prueba():
    v = [1, 2 ,3 ,4, 5]
    for i in range(0,5):
        temp = generarVecinosDeterminista(v)
        print(temp)



if __name__=="__main__":
    prueba()        