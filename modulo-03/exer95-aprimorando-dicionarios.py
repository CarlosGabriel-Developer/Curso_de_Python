#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
lista_times = []
jogador = {}
lista_partidas = []

while True:

    jogador.clear()

    jogador["Nome"] = input("Nome: ")

    num_partidas = int(input(f'Número de partidas de {jogador["Nome"]}: '))

    lista_partidas.clear()

    for i in range(num_partidas):
        lista_partidas.append(
            int(input(f'Quantos gols na partida {i+1}: '))
        )

    jogador["Gols"] = lista_partidas[:]
    jogador["Total"] = sum(lista_partidas)

    lista_times.append(jogador.copy())

    while True:
        usuario = input("Deseja continuar [S/N]? ").upper()

        if usuario in "SN":
            break

        print("Responda S ou N.")

    if usuario == "N":
        break

print("=-"*30)
print(f'{"Cod":<5}', end='')

for chave in jogador.keys():
    print(f'{chave:<15}', end='')

print()
print("=-"*30)

for k, v in enumerate(lista_times):
    print(f'{k:<5}', end='')

    for dado in v.values():
        print(f'{str(dado):<15}', end='')

    print()

print("=-"*30)

while True:

    busca = int(input("Deseja ver dados de qual jogador? (999 para sair): "))

    if busca == 999:
        break

    if busca >= len(lista_times):
        print("Código inválido!")
    else:
        print(f"\nLevantamento do jogador {lista_times[busca]['Nome']}")

        for i, g in enumerate(lista_times[busca]["Gols"]):
            print(f"No jogo {i+1} fez {g} gols.")

    print("=-"*30)

print("FIM DO PROGRAMA")