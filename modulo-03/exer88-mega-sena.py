##Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
matriz = []

user = int(input("Digite o numero de jogos que deseja que sorteie : "))

for i in range(user):
    
    jogos = []
    
    while len(jogos) < 6 : 
        
        numero = random.randint(1,60) 
        
        if numero not in jogos :
            jogos.append(numero)
            
    jogos.sort()
    matriz.append(jogos[:])


print("-"*3,end=" ")
print(f"SORTEANDO {user} JOGOS", end=" ")
print("-"*3,end=" ")
print()

for i  in range(len(matriz))  :
    
    print(f"JOGO {i+1} : {matriz[i]}")
    
print("-"*4, end=" ")
print("BOA SORTE", end=" ")
print("-"*4, end=" ")

