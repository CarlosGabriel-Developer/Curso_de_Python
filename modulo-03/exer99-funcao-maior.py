##Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(*num):
    print('Analisando os valores passados...')

    if len(num) == 0:
        print('Nenhum valor foi informado.')
        return

    maior = num[0]

    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(0.3)

        if valor > maior:
            maior = valor

    print(f'\nForam informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('-' * 30)

maior(50, 1, 5, 6, 8, 4, 9, 41, 1, 5, 54, 54, 54, 50, 674)

maior (10,32,124,21,2,13,2)