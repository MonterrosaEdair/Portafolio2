#Entradas: Una lista
#Salidas: Partir una lista a la mitad si encuentra un negativo
#Restricciones: Debe ser una lista

def mitadlista(lista):
    if isinstance(lista,list):
        if lista==[]:
            return []
        else:
            return mitad(lista,[],[])
    else:
        return "debe ser una lista"

def mitad(lista,sublista,res):
    if lista==[]:
        return res+[sublista]
    elif sublista==[]:
        return res
    else:
        if lista[0]>=0:
            return mitad(lista[1:],sublista+[lista[0]],res)
        else:
            return mitad(lista[1:],[],res+[sublista])





























        
def invertirLista(lista):
    if isinstance(lista,list):
        if lista==[]:
            return []
        else:
            return invertir(lista)
    else:
        return "Error"

def invertir(lista):
    if lista!=[]:
        return invertir(lista[1:])+[lista[0]]
    else:
        return []
    
