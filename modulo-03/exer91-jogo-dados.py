##Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint

num_jogados = []

for i in range(4):
    num_jogados.append(randint(1, 6))

print("Esses foram os números jogados:")
print(num_jogados)

maior = max(num_jogados)
vencedor = num_jogados.index(maior) + 1

print(f"O maior número foi {maior}.")
print(f"O vencedor foi o Jogador {vencedor}.")