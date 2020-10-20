#Entradas:Una lista
#Salidas: Ordenar la lista
#Restricciones: Debe ser una lista

def Ordenar(lista):
    if isinstance(lista,list):
        return Ordenar_aux(lista, [])
    else:
        return "Debe ser una lista"

def Ordenar_aux(lista, res):
    if lista == []:
        return res
    else:
        pos = Menor(lista)
        return Ordenar_aux(lista[:pos]+lista[pos+1:], res+[lista[pos]])

def Menor(lista):
    if isinstance(lista,list):
        return Menor_aux(lista[1:],lista[0],1,0)
    else:
        return "Debe ser una lista"

def Menor_aux(lista,ele, cont, pos):
    if lista==[]:
        return pos
    else:
        if lista[0][0] < ele[0]:
            return Menor_aux(lista[1:], lista[0], cont+1, cont)
        else:
            return Menor_aux(lista[1:], ele, cont+1, pos)
