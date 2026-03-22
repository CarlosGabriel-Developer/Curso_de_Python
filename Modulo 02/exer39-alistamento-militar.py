#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Ano de nascimento : '))

if (ano_atual-ano_nascimento == 18):
    print(f"Nascidos em {ano_nascimento}")
    print("Você precisa alistar ao serviço militar urgente")
    
elif(ano_atual-ano_nascimento > 18):
    print(f"Nascidos em {ano_nascimento}já prestaram o alistamento, você prestou serviço em {ano_nascimento+18}")
    print("Você já prestou o serviço militar")
    
else:
    print(f"Nascidos em {ano_nascimento}")
    print(f"Você ainda é novo para prestar o serviço militar,falta {18 - (ano_atual-ano_nascimento) } anos ainda")
    print(f"Você vai se alistar no ano de {ano_nascimento+18}")