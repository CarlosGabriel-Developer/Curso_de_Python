##Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

import random

print("-="*40)
print("VAMOS JOGAR IMPAR OU PAR")
print("-="*40)

while True :
    
    user = int(input("Digite um numero [0-10] : "))
    
    computador = random.randint(0,10)
    
    soma = user + computador
    
    tipo = " "
    
    while tipo not in "PI" :
        
        tipo = str(input("PAR OU IMPAR [I/P] : ")).upper()[0]

    print(f"Você jogou {user} e o computador escolheu {computador}. A soma deu {soma} o jogador escolheu {tipo} ",end="")
    print("DEU PAR" if soma % 2 == 0 else "DEU IMPAR")
    
    if tipo == "P":
        
        if soma %2 == 0 : 
            
            print("VOCÊ VENCEU")
            
        else : 
            
            print("VOCÊ PERDEU")
            
            break
    
    elif tipo == "I" : 
        
        if soma %2 == 1 :
            
            print("VOCÊ VENCEU")
            
        else : 
            
            print("VOCÊ PERDEU")
            
            break
        
    print("VAMOS JOGAR NOVAMENTE")
    
