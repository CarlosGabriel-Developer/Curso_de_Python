##Faça um programa que leia 5 números e informe o maior número.


maior = 0

for i in range(5) : 
    
    num = int(input("Digite um numero : "))
    
    if i == 0 : 
        
        maior = num
        
    elif num > maior : 
        
        maior = num
            

print(f"O maior numero é {maior}")