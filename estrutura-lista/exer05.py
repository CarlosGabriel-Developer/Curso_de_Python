#Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

todos_numeros = []
numeros = [[],[]]

for i in range(20) : 
    
    num = int(input("Numero : "))
    
    todos_numeros.append(num)
    
    if num % 2 == 0 : 
        numeros[0].append(num)
        
    else : 
        numeros[1].append(num)
        
print("Numeros Pares")               
print(numeros[0])

print("Numeros impares")
print(numeros[1])

print("Todos os valores")
print(numeros)