##Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dicionario = {}

dicionario["Nome"] = str(input("Digite o seu nome : "))
dicionario["Media"] = float(input("Digite a sua média : ")) 

for k, v in dicionario.items() : 
    
    print(f"{k} do aluno é {v}")
    