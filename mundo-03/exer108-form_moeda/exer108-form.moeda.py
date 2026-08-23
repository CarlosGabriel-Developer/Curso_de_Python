##Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda


valor = float(input('Digite um valor: '))

print(f'A metade de {valor} é {moeda.metade(valor)}')


print(f'O dobro {valor} é {moeda.dobro(valor)}')


print(f'Aumentando 10% de {valor} é {moeda.aumentar(valor,10)}')


print(f'Diminuir 13% de {valor} é {moeda.diminuir(valor,13)}')





