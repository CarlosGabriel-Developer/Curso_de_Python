

def voto(idade) : 
  
    from datetime import datetime
    
    ano_atual = datetime.today().year
    
    idade = ano_atual - ano_nacismento
    
    print(f'A sua idade é {idade}')
    
    if idade >= 18 : 
        
        return f'O voto é obrigatorio com {idade}'




ano_nacismento = int(input('Ano de Nacimento'))

print(voto(ano_nacismento))