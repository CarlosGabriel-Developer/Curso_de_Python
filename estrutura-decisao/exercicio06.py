##Exercício 06Faça um programa que leia três números e mostre o maior deles:

maior = 0 


for i in range (1,4,1) :
    
    numero = int(input(f"Digite o um numero [{i}] : "))
    
    if i == 1 :
        
        maior = numero 
        
    else :
        
        if numero > maior :
            maior = numero
        

print(f"O maior numero é o {maior}")