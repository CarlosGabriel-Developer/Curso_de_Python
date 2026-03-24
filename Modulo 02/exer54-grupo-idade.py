#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date



maiores_idade = menores_idade = 0 
ano_atual = date.today().year

for i in range(1,8):
    
    pessoa = int(input(f"Digite o seu ano de nacimento da pessoa {i} : "))
    idade_pessoa = (ano_atual-pessoa)
    
    if idade_pessoa <= 18 :
        menores_idade+= 1
        
    else :
        maiores_idade += 1
        
print(f"O numero de pessoas que tem a maioridade de idade é de {maiores_idade}")

print(f"O numero de pessoas que não possui a maioridade de idade é de {menores_idade}")