#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

contador = 0
print()
num = int(input("Digite um numero : "))
print()

for i in range(1,num+1):

    if num % i == 0:
        print(f"\033[0;31m{i}", end=",")
        contador += 1 
        
    else :
        print(f"\033[0;34m{i}", end=",")
        

print(f"\n\033[mO numero {num} foi divisivel {contador} vezes")

if contador == 2 :
    print("Esse numero é primo")
        
else:
    print("Esse numero não é primo")
