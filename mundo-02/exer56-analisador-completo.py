#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idade_soma_grupo = idade_media_grupo = idade_homem = numero_mulheres = 0 

nome_homem_mais_velho = ""


for i in range(1,5):
    
    print(f"Pessoa {i}")
    
    nome = str(input(f"Digite o nome pessoa {i} : "))
    
    idade = int(input(f"Idade da pessoa {i} : "))

    sexo = str(input("O seu sexo é [M ou F] : "))
    
    idade_soma_grupo += idade
   
    if i == 1 and sexo in "Mm" : 
        
        idade_homem = idade
        nome_homem_mais_velho = nome
        
    elif idade > idade_homem :
        idade_homem =idade
        nome_homem_mais_velho = nome
            
            
            
    if sexo in "Ff" and idade < 20 :

        numero_mulheres += 1
    
        
        
    
    print("="*20)
    
    
    
    
print(f"A idade média do grupo é de {idade_soma_grupo/4}")

print(f"O homem mais velho é o {nome_homem_mais_velho} e sua idade é {idade_homem}")

print(f"O numero mulheres com menos de 20 anos é de {numero_mulheres}")
    
