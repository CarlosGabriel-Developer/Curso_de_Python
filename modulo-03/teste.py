

def voto(idade) : 
  
    from datetime import datetime
    
    ano_atual = datetime.today().year
    
    idade = ano_atual - ano_nacismento
    
    print(f'A sua idade é {idade} anos')
    
    if idade >= 18 : 
        
        return f'O voto é obrigatorio com {idade} anos'
    
    elif 16 <= idade or idade >= 65 : 
        
        return f'O voto com  a idade de {idade} anos é opcional'
    
    else : 
        
        return 'O voto ainda não possivel'




ano_nacismento = int(input('Ano de Nacimento: '))

print(voto(ano_nacismento))