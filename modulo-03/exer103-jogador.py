##Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha (nome='<desconhecido>',gol=0) : 
    
    print(f'O jogador {nome} fez {gol} gols ')
    
    

nomes = str(input('Nome:')).capitalize()

gols = str(input('Numero do gols: '))

if gols.isnumeric() : 
    gols = int(gols)
    
else : 
    gols = 0 
    
if nomes.strip() == '' : 
    ficha(gol=gols)
    
else : 
    ficha(nomes,gols)