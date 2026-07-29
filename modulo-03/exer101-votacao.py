from datetime import datetime


ano_atual = datetime.now().year


def voto(ano_nascimento) : 
    
    idade_atual = ano_atual- ano_nascimento


    if 18<= idade_atual <= 64 : 
        return f"Com {idade_atual} o voto é obrigatorio"

    elif idade_atual >= 65 :
        return f"Com {idade_atual} o voto é opcionoal"
    
    else : 
        return "Não está autorizado o voto"
    
    
    
usuario = int(input('Ano de Nascimento'))

print(voto(usuario))
        

