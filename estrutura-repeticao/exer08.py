##Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0 

for i in range(0,5,1) : 
    
    num = int(input("Digite um numero : "))
    
    soma += num

media = soma/5

print(f"A soma de todos os valores digitados foi de {soma} e a média foi de {media}")