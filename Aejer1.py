

"""

1. Escriba un algoritmo que solicite cuatro números y 
calcule la media aritmética (promedio) entre ellos.

"""


def Promedio(num1,num2, num3, num4):
    return (num1+num2+num3+num4)/4



num1 = int(input("Ingrese un numero :"))
num2 = int(input("Ingrese un numero :"))
num3 = int(input("Ingrese un numero :"))
num4 = int(input("Ingrese un numero :"))

print("El promedio es :" + Promedio(num1,num2,num3,num4))