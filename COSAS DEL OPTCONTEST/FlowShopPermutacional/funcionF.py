def funcionF(v, m):
    
    solucion = [None] * len(m)

    tiempo = [0] * len(m[0])
    
    for x in v:
        for i in range(len(m[0])):
            if i > 0:
                if (tiempo[i-1] + m[x][i]) < (tiempo[i] + m[x][i]):
                    tiempo[i] = tiempo[i] + m[x][i]
                else:
                    tiempo[i] = tiempo[i-1] + m[x][i]
            else:
                tiempo[i] = tiempo[i] + m[x][i]
            

        solucion[x] = tiempo.copy()
            
    return solucion