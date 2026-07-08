#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

soma_gols = 0 

dicionario = {}

dicionario['Nome'] = str(input("Nome : "))
dicionario['Numero_partidas'] = int(input("Numero de Partidas jogadas : "))

if dicionario['Numero_partidas'] > 0 : 
    
    for i in range(dicionario['Numero_partidas']) : 
        num_gols = int(input(f"Quantos gols foram marcados na partida {i+1} : "))
        soma_gols += num_gols
        
        dicionario['Numero_total_gols'] = soma_gols
        
print('-='*40)

for k,v in dicionario.items() : 
    print(f'A chave {k} tem o valor {v}')