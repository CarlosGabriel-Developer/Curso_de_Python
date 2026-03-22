#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma_numPares = 0
contador = 0


for i in range(1,7):
    num = int(input("Digite um numero :"))
    
    if num % 2 == 0 : 
        contador += 1 
        soma_numPares += num
            
print(f"Você digitou {contador}\nA soma dos numeros pares foi de {soma_numPares}")
        
        
    
    