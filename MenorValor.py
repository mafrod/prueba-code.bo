#Encuetra el menor valor en una lista

def Menor(lista):
    n = 0
    for i in range(len(lista)):
        if lista[i] > n:
            n = lista[i]
    n = n + 1 
    print(n)  
        
lista = [-1, -3]
Menor(lista)
