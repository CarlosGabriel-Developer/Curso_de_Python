#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


dicionario = {}
lista_gols = []

lista_jogadores = {}

while True : 
    
    nome = str(input('Nome: ')).capitalize()
    
    dicionario['Nome'] = nome
    
    numero_partidas = int(input('Numero de partidas jogadas :'))
    
    dicionario['Partidas'] = numero_partidas
        
    for jogo in range(dicionario['Partidas']):

        gol = int(input(f'Gols marcados na partida{jogo+1} :'))
        
        if gol >= 0 :
            
            lista_gols.append(gol)
        
        else :
            print('Tente novamente')
            
    dicionario['Gols'] = lista_gols
    
    dicionario['Total'] = sum(lista_gols)
        

    lista_jogadores = dicionario
        
    usuario = str(input('Deseja continuar [S/N] :')).upper()[0]
    
    if usuario in 'N' : 
        break
    
print('=-'*40)

for i in lista_jogadores :
    print(f'{i}',end=':>20f')