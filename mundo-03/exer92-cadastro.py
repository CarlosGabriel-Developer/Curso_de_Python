##Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
# now = datetime.now()
# today = now.date()

ano_atual = datetime.now().year

dicionario = {}

dicionario['Nome'] = str(input("Nome : "))
dicionario['Ano_nascimento'] = int(input("Ano de nascimento : "))
dicionario['Idade_atual'] = ano_atual - dicionario['Ano_nascimento']
dicionario['Num_carteira'] = int(input("Numero da carteira de trabalho [0 não tiver]: "))

if dicionario['Num_carteira'] != 0 : 
    
    dicionario['Ano_contratacao'] = int(input("Ano de Contratação : "))
    dicionario['Salario'] = int(input("Salario : "))
    dicionario['Ano_aposetadoria'] = dicionario['Ano_contratacao'] + 35
    dicionario['Idade_aposetadoria'] = dicionario['Idade_atual'] + dicionario['Ano_aposetadoria'] - ano_atual
    
print("="*40)

for k,v in dicionario.items() : 
    
    print(f"{k} tem o valor de {v}")