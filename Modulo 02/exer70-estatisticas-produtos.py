#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato. 


valor_produto = valor_total = produtos_mais_mil = produto_mais_barato = 0
nome_produto_barato = " "



while True : 
    
    print("="*40)
    
    nome_produto = str(input("Nome do produto : "))
    
    valor_produto = float(input("Valor do produto : "))
    valor_total += valor_produto
    
    if valor_produto >= 1000 : 
        
        produtos_mais_mil += 1 
        
    if valor_produto < produto_mais_barato :
        
        produto_mais_barato = valor_produto
        nome_produto_barato = nome_produto
    

    print("="*40)
    
    respota = " "
    
    while respota not in "SsNn" : 
        
        respota = str(input("Deseja continuar [S/N] : "))
        
    if respota in "Nn" : 
        
        break
    

print(f"O valor total das compras foi de R$ {valor_total}")

print(f"Foram cadastrados {produtos_mais_mil} produtos acima de R$1000 de valor")

print(f"O produto mais barato é o {nome_produto_barato} e o seu valor é R$ {produto_mais_barato}")