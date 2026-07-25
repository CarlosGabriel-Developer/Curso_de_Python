#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(inicio, fim, passo):

    if passo == 0:
        passo = 1

    passo = abs(passo)

    print(f'{inicio} até {fim} no passo de {passo}')

    contador = inicio

    if inicio > fim:
        while contador >= fim:
            print(contador, end=' - ')
            contador -= passo

    else:
        while contador <= fim:
            print(contador, end=' - ')
            contador += passo

    print('FIM')
    
usuario_incio = int(input('Numero inicio : '))
    
usuario_fim = int(input('Numero final : '))
    
usuario_passo = int(input('Passo : '))
            
contador(0,10,1)

contador(10,0,2)

contador(usuario_incio,usuario_fim,usuario_passo)