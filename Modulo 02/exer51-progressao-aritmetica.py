#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão



termo_A1 = int(input("Primeiro termo :"))
razão = int(input("Razâo :"))

termo_A10 = termo_A1 + (10-1) * razão

for i in range(termo_A1,termo_A10+razão,razão):
    print(f"{i}", end="==>")
    
print("ACABOU")