##Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

cont_pares = cont_impares = 0

for i in range(0,10,1) : 
    
    num = int(input("Digite um numero : "))
    
    if num % 2 == 0 : 
        cont_pares += 1 
        
    else : 
        cont_impares += 1 
    
print(f"O contador de numero impares é igual a {cont_impares}")
print(f"O contador de numeros pares é igual a {cont_pares}")