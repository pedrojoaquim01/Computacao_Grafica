from array import array

def solidoFuncional(fv,N):

    v = array('f',[])
    t = array('f',[])

    def ft(i,j):
        return i/N, j/N

    def adiciona(lista,vertice):
        for v in vertice:
            lista.append(v)

    for i in range(N):
        for j in range(N):
            vA = fv(i,j)
            tA = ft(i,j)
            vB = fv(i,j+1)
            tB = ft(i,j+1)
            vC = fv(i+1,j+1)
            tC = ft(i+1,j+1)
            vD = fv(i+1,j)
            tD = ft(i+1,j)
            adiciona(v,vA)
            adiciona(t,tA)
            adiciona(v,vB)
            adiciona(t,tB)
            adiciona(v,vD)
            adiciona(t,tD)
            adiciona(v,vB)
            adiciona(t,tB)
            adiciona(v,vC)
            adiciona(t,tC)
            adiciona(v,vD)
            adiciona(t,tD)
    return v, t



