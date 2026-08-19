#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(inicio, fim, passo):

    if passo < 0: 
        passo *= -1
        
    if passo == 0 : 
        passo = 1

    print('='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    
    if inicio < fim :
        
        i = inicio
        
        while i <= fim : 
            print(f'{i}', end=' ')
            i += passo    
        print('FIM')
        
    else : 
        
        i = inicio
        
        while i >= fim :
            print(f'{i}', end=' ')
            i -= passo
        print('FIM')
        
contador(10,0,1)
contador(0,10,1)
contador(100,0,-2)