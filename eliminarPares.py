#Entradas: Una lista
#Salidas: Eliminar los números pares de una lista
#Restricciones: Debe ser una lista

def eliminarPares(lista):
    if isinstance (lista,list):
        if lista==[]:
            return []
        else:
            return eliminarParesAux(lista,[],[],[])


def eliminarParesAux(lista,sublista,impares,res):
    if lista==[]:
        if sublista==[]:
            return res
        else:
            return res+[sublista]
    elif lista[0]>=0:
        print(lista[0])
        if lista[0]%2==1:
            return eliminarParesAux(lista[1:],sublista+[lista[0]],impares,res)
        else:
            return eliminarParesAux(lista[1:],sublista,impares,res)
