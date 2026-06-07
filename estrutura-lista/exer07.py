#Faça um programa que leia um vetor de 4 números inteiros, mostre a soma, a multiplicação e os números.

num = []

for i in range(4):
    
    num.append(int(input("Digite um numero : ")))
    

soma = 0
mult = 1 

for i in num : 
    
    soma += i
    mult *= i
    
print(f"Números:{num}")
print(f"Soma:{soma}")
print(f"Multiplicação:{mult}")