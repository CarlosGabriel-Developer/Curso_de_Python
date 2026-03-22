#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

contador = 0
num = int(input("Digite um numero : "))

for i in range(1,num+1):
    
    if num % i == 0:
        print(f"\033[0;31m{i}", end=",")
        
