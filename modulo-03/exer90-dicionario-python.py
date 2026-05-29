##Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dicionario = {}

dicionario["Nome"] = str(input("Digite o seu nome : "))
dicionario["Media"] = float(input("Digite a sua média : "))

if dicionario["Media"] >= 7 : 
    dicionario["Situação"] = 'Aprovado'
    
elif 5 < dicionario["Media"] < 7 : 
    dicionario["Situação"] = 'Recuperção'
    
else : 
    dicionario["Situação"] = 'Recuperado'

for k, v in dicionario.items() : 
    
    print(f"{k} do aluno é {v}")

    