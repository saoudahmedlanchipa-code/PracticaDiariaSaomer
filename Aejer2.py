"""
Escribir un algoritmo que solicite tres números
 y calcule las medias aritmética y geométrica (G).
"""

def Aritmetica(n1,n2,n3):
    return  str((n1+n2+n3)/3)

def Geometrica(n1,n2,n3):
    return str((n1*n2*n3) ** (1/2))

num1 = float(input("Ingresa num1: "))
num2 = float(input("Ingresa num1: "))
num3 = float(input("Ingresa num1: "))


print("El promedio es :" + Aritmetica(num1,num2,num3))
print("la media geometrica es :" + Geometrica(num1,num2,num3))
