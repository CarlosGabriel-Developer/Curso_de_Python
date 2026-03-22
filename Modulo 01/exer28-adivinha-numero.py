import random

computador = random.randint(1,5)

jogador = int(input("Escolha um numero de [1-5] : "))

print(f"Você escolheu numero: {jogador}")
print(f"O Computador escolheu {computador}")

if jogador == computador:
    
    print("Parabens você venceu !!")
    
else: 
    print("Voce errou")