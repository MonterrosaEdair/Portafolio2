#Entradas: Una lista
#Salidas: Partir una lista a la mitad y dividir los pares e impares
#Restricciones: Debe ser una lista

def paresImpares(lista):
    if isinstance (lista,list):
        if lista==[]:
            return []
        else:
            return paresImparesAux(lista,[],[],[])

def paresImparesAux(lista,sublista,impares,res):
    if lista==[]:
        if sublista==[]:
            return res
        else:
            return res+[sublista]
    elif lista[0]>=0:
        print(lista[0])
        if lista[0]%2==1:
            return paresImparesAux(lista[1:],sublista+[lista[0]],impares,res)
        else:
            return paresImparesAux(lista[1:],sublista,impares,res)
