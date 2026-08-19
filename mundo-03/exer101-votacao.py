#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano_nascimento) : 
    from datetime import datetime
    ano_atual = datetime.now().year

    idade_atual = ano_atual - ano_nascimento

    if idade_atual < 16 : 
        return f'Com {idade_atual} anos : Não vota'
    
    elif 16 <= idade_atual <=18 or idade_atual > 65 :
        return f'Com {idade_atual} anos : O voto é opcional'
    
    else:
        return f'Com a {idade_atual} anos. O voto é obrigatorio'
            
    
    
    
usuario = int(input('Ano de Nascimento: '))

print(voto(usuario))
        

