#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda


valor = float(input('Digite um valor: '))

print(f'A metade de {valor} é {moeda.metade(valor,True)}')


print(f'O dobro {valor} é {moeda.dobro(valor,True)}')


print(f'Aumentando 10% de {valor} é {moeda.aumentar(valor,10,True)}')


print(f'Diminuir 13% de {valor} é {moeda.diminuir(valor,13,False)}')





