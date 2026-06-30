#Faça um programa que leia três números e mostre-os em ordem decrescente:

lista = []

for i in range(3) :
    
    produto = int(input("Valor do produto :"))
    lista.append(produto)
    
print(sorted(lista))