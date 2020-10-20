#Entradas: Un número
#Salidas: Partir una lista a la mitad y dividir los pares con los impares y mostrar los en una lista con sublistas
#Restricciones: Debe ser una lista

def descomponerNumeros(num):
    if isinstance (num,int):
        if num==0:
            return 0
        else:
            return descomponerNumerosAux(num,[],[],0)

def descomponerNumerosAux(num,sublista,impares,res):
    if num==0:
        if sublista==[]:
            return res
        else:
            return [sublista]+[impares]
    elif num>=0:
        print(num)
        if (num%10)%2==0:
            return descomponerNumerosAux(num//10,sublista+[num%10],impares,res+1)
        else:
            return descomponerNumerosAux(num//10,sublista,impares+[num%10],res)

