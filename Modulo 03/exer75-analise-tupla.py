##Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

num1 = int(input("digite um numero entre 0-9 : "))
num2 = int(input("digite um numero entre 0-9 : "))
num3 = int(input("digite um numero entre 0-9 : "))
num4 = int(input("digite um numero entre 0-9 : "))

numeros_tupla = (num1,num2,num3,num4)

print(f"Quantas vezes apareceu o valor 9 : {numeros_tupla.count(9)} veze(s)")

if 3 in numeros_tupla : 
    print(f"Em que posição do index foi digitado: {numeros_tupla.index(3)}")
else : 
    print("O numero 3 não foi informado á tupla")

print(f"Quais foram os números pares: ",end=" ") 
for i in numeros_tupla : 
    
    if i % 2 == 0 :
        
        print(i,end=" ")