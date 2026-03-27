##Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

computador = random.randint(0,10)
tentativa = 0 
jogador = int(input("Digite um numero [0-10] : "))


while jogador != computador : 
    
    print("Você errou, Tente novamente")
    print()
    jogador = int(input("Digite um numero [0-10] : "))
    tentativa += 1 
    
print(f"Você acertou o numero do computador {computador} com {tentativa} tentativas")
    
    