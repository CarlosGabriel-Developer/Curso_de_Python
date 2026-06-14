##Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

numero = int(input("Numero : "))

fatorial = 1

print(f"{numero}! = ", end='')

for i in range(numero,0,-1) : 
    fatorial *= i
    
    if i == 1 : 
        print(i, end='')
        
    else : 
        print(i, end=".")

print(f" = {fatorial}")