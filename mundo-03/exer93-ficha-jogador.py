#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dicionario = {}
lista_gols = []

dicionario['Nome'] = input("Nome: ")
dicionario['Numero_partidas'] = int(input("Número de partidas jogadas: "))

for i in range(dicionario['Numero_partidas']):
    lista_gols.append(int(input(f"Quantos gols foram marcados na partida {i+1}: ")))

dicionario['gols'] = lista_gols
dicionario['Total'] = sum(lista_gols)

print('-=' * 40)

for k, v in dicionario.items():
    print(f'{k}: {v}')