#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

    # Quantidade de notas
    # A maior nota
    # A menor nota
    # A média da turma
    # A situação (opcional)


def notas(*nota,sit=False) : 
    
    ''''''
    
    dados = {}
    
    dados['Total'] = len(nota)
    dados['Maior'] = max(nota)
    dados['Menor'] = min(nota)
    dados['Media'] = sum(nota)/len(nota)
    
    if sit == True :
        if dados['Media'] >= 7 :
            dados['Situação'] = 'BOA'
            
        elif dados['Media'] >= 5 :
            dados['Situação'] = 'RAZOAVEL'
            
        else :
            dados['Situação'] = 'RUIM'
            
    return dados
    

usuario = notas(23,2,12,3,sit=True)

print(usuario)