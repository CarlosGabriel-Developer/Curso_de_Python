#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(ar1, ar2, ar3):
    return ar1 + ar2 + ar3

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

resultado = soma(num1, num2, num3)

print("Soma:", resultado)