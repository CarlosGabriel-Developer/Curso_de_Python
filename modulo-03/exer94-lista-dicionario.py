#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dicionario_pesso = {}
lista_todas_pessoas = []


while True :
    
    dicionario_pesso['Nome'] = str(input('Nome: ')).lower()
    
    while True :
        sexo = str(input('Sexo: [M/F] ')).upper()
        
        if sexo in "MmFf" :
            dicionario_pesso['Sexo'] = sexo
            break
            
        else :
            print("Tente novamente")
            
    while True : 
            
        idade = int(input('Idade: '))
        if 0 < idade < 120 :
            dicionario_pesso['Idade'] = idade
            break
            
        else : 
            print('Tente Novamente')


    lista_todas_pessoas.append(dicionario_pesso.copy())

    usuario = input('Deseja continuar? [S/N] ').upper()

    if usuario == 'N':
        break

print('=-'*40)

print(f'A) Quantas pessoas foram cadastradas : ({len(lista_todas_pessoas)} pessoas)')
soma_idades = 0

for pessoa in lista_todas_pessoas : 
    
    soma_idades += pessoa['Idade']
    
media = soma_idades/len(lista_todas_pessoas)
        
print(f'B) A média de idade {media:.2f}')


lista_todas_mulheres = []

for pessoa in lista_todas_pessoas : 
    if pessoa["Sexo"] == "F" :  
        lista_todas_mulheres.append(pessoa)
        
print("# C) Uma lista com as mulheres")
print(lista_todas_mulheres)


lista_todas_pessoas_acima_media = []

for pessoa in lista_todas_pessoas : 
    
    if pessoa["Idade"] > media : 
        lista_todas_pessoas_acima_media.append(pessoa)
        
print('D) Uma lista de pessoas com idade acima da média')
print(lista_todas_pessoas_acima_media)