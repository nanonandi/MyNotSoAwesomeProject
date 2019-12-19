# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:42:47 2018

@author: David Cacho Saiz
@author: Fernando Antón Ortega
"""

import numpy as np
import funcionF as f
import Evaluar as ev
import BusquedaAleatoria as aleat
import BusquedaPrimerMejor as prime
import Recocido as reco
#import Genetico as gene





print ("********************************")
print ("***  PROBLEMAS DE FLOW SHOP  ***")
print ("***        PERMUTACIONAL     ***")
print ("********************************")
print ("")
print ("Introduzca el fichero que quiere leer")
fichero = input()
#fichero = ("d/ejem_clase1.txt")
matriz = []

fich = open (fichero, "r")
oym = fich.readline().strip().split()

ordenes = oym[0]
maquinas = oym[1]

matriz = np.genfromtxt(fich, int)
matriz = np.delete(matriz, np.s_[::2], 1)
fich.close()

busqueda_aleatoria,t1 = (aleat.busquedaAleatoria(len(matriz),matriz))
print ("Busqueda aleatoria: "+ str(busqueda_aleatoria))
f1 =(f.funcionF(busqueda_aleatoria,matriz))
for x in f1:
    print(x)
print ("Tiempo de salida: "+str(t1)+"s")    

busqueda_primer_mejor,t2 = prime.primerMejor(len(matriz),matriz)
print ("Busqueda primer mejor: "+ str(busqueda_primer_mejor))
f2 = (f.funcionF(busqueda_primer_mejor,matriz))
for x in f2:
    print(x)
print ("Tiempo de salida: "+str(t2)+"s") 

busqueda_recocido,t3 = reco.recocido(len(matriz),matriz)
print ("Busqueda recocido: "+ str(busqueda_recocido))
f3 = (f.funcionF(busqueda_recocido,matriz))
for x in f3:
    print(x)
print ("Tiempo de salida: "+str(t3)+"s") 

"""
busqueda_genetico,t4 = gene.genetico(len(matriz),matriz)
print ("Busqueda genetico: "+ str(busqueda_genetico))
f3 = (f.funcionF(busqueda_genetico,matriz))
for x in f4:
    print(x)
print ("Tiempo de salida: "+str(t4)+"s") 
"""




oym = None
#print ("Ordenes: " + ordenes)
#print ("Maquinas: " + maquinas)
#print ("Matriz: ")
#for x in matriz:
#    print (x)