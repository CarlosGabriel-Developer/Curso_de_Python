#Faça um programa com uma função chamada soma_imposto. A função possui dois parâmetros formais: taxa_imposto, que é a quantia de imposto sobre vendas expressas em porcentagem, e custo, que é o custo de um item antes do imposto. A função "altera" o valor de custo para incluir o imposto sobre vendas.

def soma_imposto(taxa_imposto, custo):
    total = custo + (custo * taxa_imposto / 100)
    print(total)

soma_imposto(10, 10)

    
    
