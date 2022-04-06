#Identificar si una cadena es Palíndrome

def Palindrome(cadena):
    if str(cadena) == "".join(reversed(cadena)): #Recibimos una cadena como parámetro, comparamos la misma cadena con su inversa
        print("La cadena es Palindrome")
    else:
        print("La cadena no es Palindrome")

Palindrome("hola")
