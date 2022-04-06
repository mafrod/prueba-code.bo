#Generamos la serie fibonaci de un número

def Fibonaci(numero):
    a = 0 #valor inicial de la serie
    b = 1 #valor inicial de la serie
    fibo = 0 #valor de la serie
    i = 1
    print("La serie fibonaci de ", numero, "es: ")
    
    while(i <= numero):
        print(fibo)
        a = b
        b = fibo
        fibo = a + b
        i += 1

Fibonaci(4)