#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano_nascimento) : 
    from datetime import datetime
    ano_atual = datetime.now().year

    idade_atual = ano_atual- ano_nascimento


    if 18 <= idade_atual <= 64 : 
        return f"Com {idade_atual} o voto é obrigatorio"

    elif 16 <= idade_atual < 18 or idade_atual >= 70:
        return f"Com {idade_atual} anos, o voto"
    
    else:
        return f"Com {idade_atual} anos, você ainda não pode votar."
    
    
    
usuario = int(input('Ano de Nascimento'))

print(voto(usuario))
        

