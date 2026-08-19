##Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

maior = menor = 0
num = []

for i in range(1,6): 
    numero = int(input("Digite um numero : "))
    num.append(numero)
    print('Numero adicionado')

print('-'*20)    
print(num)
print('-'*20)

for i,v in enumerate(num) : 

    if i == 0 : 
        
        maior = menor = v 
        
    else : 
        
        if v < menor : 
            
            menor = v

            
            
        elif v > maior : 
            
            maior = v 
            
       

print(f"O maior numero da lista foi :{maior}")
print('Index :', end='') 

for i ,v in enumerate(num) : 
    if v == maior : 
        print(i)
 
print('-'*20)

print(f"O menor numero da lista foi :{menor}") 
print('Index :', end='') 

for i ,v in enumerate(num) : 
    if v == menor : 
        print(i)     