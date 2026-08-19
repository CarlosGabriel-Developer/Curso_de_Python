##Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


tupla = (
 
        'hoje', 'azul', 'parte', 'coragem', 'computador', 'carro',
         'cachorro', 'jabuticaba', 'jericoacoara', 'filtro'

)

vogais = 'aeiou'

for palavra in tupla:
    print(f'\nNa palavra "{palavra}" temos as vogais: ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')