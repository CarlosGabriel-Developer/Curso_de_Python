##Exercício 08 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:

menor_valor = 0 

for i in range(1, 4):
    
    produto = float(input("Digite o valor do produto: "))
    
    if i == 1: 
        menor_valor = produto
    else: 
        if produto < menor_valor:
            menor_valor = produto

print(f"O menor produto é o do valor de {menor_valor}")