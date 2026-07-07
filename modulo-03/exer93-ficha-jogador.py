#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


lista = []

dicionario = {}

dicionario['Nome'] = str(input('Nome : '))
dicionario['Numero_partidas'] = int(input('Numero de Partidas : '))

if dicionario['Numero_partidas'] > 0 :
    
    for i in range(dicionario['Numero_partidas']) : 
        
        dicionario['gols_partidas'] = int(input(f'Quantos gols na partida {i} : '))
        