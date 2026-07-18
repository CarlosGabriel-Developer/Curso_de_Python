##Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(*num) : 
    
    
    Maior = num[0]
    
    for i  in num : 
        if i > Maior : 
            Maior = i

    print(f'Foram informados {len(num)} numeros')
    print(f'E o maior numero é o {Maior}')
            
    
    
maior(50,1,5,6,8,4,9,41,1,5,54,54,54,50,674)