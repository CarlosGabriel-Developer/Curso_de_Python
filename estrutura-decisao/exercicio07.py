##Exercício 07Faça um programa que leia três números e mostre o maior e o menor deles:

maior = menor = 0 

for i in range (1,4,1) : 
    
    numero = int(input("Digite um numero : "))
    
    if i == 1 : 
        
        maior = menor = numero 
        
    else : 
        
        if numero > maior : 
            maior = numero
        
        if numero < maior : 
            numero = menor
            

print(f"O maior numero é {maior}")
print(f"O menor numero é {menor}")

