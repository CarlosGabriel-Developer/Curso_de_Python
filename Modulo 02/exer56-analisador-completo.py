#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = mulher = homem = 0
nome_homem_mais_velhor = ()

for i in range(1,5):
    print(f"Pessoa {i}")
    
    nome = str(input(f"Digite o nome pessoa {i} : "))
    
    idade = int(input(f"Idade da pessoa {i} : "))
        
    sexo = str(input("O seu sexo é [M ou F] : ")).upper()
    
    print("="*20)
    
    

    
    
print(f"A media do grupo de pessoas é de {soma_idade/4}")
print(f"O homen mais velho é o {nome_homem_mais_velhor}")