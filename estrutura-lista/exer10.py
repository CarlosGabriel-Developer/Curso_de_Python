##Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

import random

lista1 = []
lista2 = []
lista3 = []

for i in range (10) :
    
    num = random.randint(1,100)
    lista1.append(num)
        
for i in range(10) : 
    
    num = random.randint(1,100)
    lista2.append(num)
    
for i in range(10) : 
    
    lista3.append(lista1[i])
    lista3.append(lista2[i])
    
    

print(f"Lista 1 : {lista1}")
print(f"\nLista 2 : {lista2}")
print(f"\nLista 3 : {lista3}")