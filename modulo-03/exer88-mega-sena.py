##Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
matriz = []

user = int(input("Quantos jogos vpcê quer que eu sorteie : "))


#gerador de numeros
for i in range(user) : 
    
    jogos = []
    
    for i in range (0,6,1) : 
        
        jogos.append(random.randint(1,60))
        
    matriz.append(jogos[:])
    jogos.clear()



print("-"*3,end=" ")
print(f"SORTEANDO {user} JOGOS", end=" ")
print("-"*3,end=" ")
print()

for i  in range(len(matriz))  :
    
    print(f"JOGO {i+1} : {matriz[i]}")
    
print("-"*4, end=" ")
print("BOA SORTE", end=" ")
print("-"*4, end=" ")

