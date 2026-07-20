##Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint


def sorteia(lista) :
    print('Os 5 valores sorteados foram os : ', end='')
    
    for i in range(0,5) : 
        numero = randint(1,10)
        lista.append(numero)
        print(f'{numero}', end=' ')
    print('Fim')
        
        
        
def somaPar(lista) :
    
    soma = 0
    
    for i in lista : 
        
        if i % 2 == 0 : 
            soma += i 
            
    print(f'A soma dos numero par foi de {soma}')



numeros = []

sorteia(numeros)
somaPar(numeros)