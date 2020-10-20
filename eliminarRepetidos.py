#Entradas: Una lista
#Salidas: Eliminar los números repetidos de una lista
#Restricciones: Debe ser una lista


def eliminarRepetidos(lista):
    if isinstance (lista,list):
        if lista==[]:
            return []
        else:
            return eliminarRepetidosaux(lista,[],[],[])


def eliminarRepetidosaux(lista,sublista,repetidos,res):
    if lista==[]:
        if sublista==[]:
            return res
        else:
            return res+[sublista]
    elif isinstance(lista[0],int) or isinstance(lista[0],float) or isinstance(lista[0],str):
        print(lista[0])
        if lista[0]!=lista[-1]:
            return eliminarRepetidosaux(lista[1:],sublista+[lista[0]],repetidos,res)
        else:
            return eliminarRepetidosaux(lista[1:],sublista,repetidos,res)
