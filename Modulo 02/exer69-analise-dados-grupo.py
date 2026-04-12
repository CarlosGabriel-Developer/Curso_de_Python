##xercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.


num_18 = num_homens = num_mulhers_20 = 0


while True : 
    
    print("="*40)
    
    idade = int(input("Digite a sua idade : "))
    
    sexo = " "
    
    while sexo not in "MF" :
        
        sexo = str(input("Sexo [M/F] : ")).strip().upper()[0]
        
    if idade > 18 : 
        num_18 += 1 
        
    if sexo in "Mm" : 
        num_homens += 1 
        
    if sexo in "Ff" and idade < 20 : 
        num_mulhers_20 += 1 
        
    
    resposta = " " 
    
    print("="*40)
    
    while resposta not in "SsNn" : 
        
        resposta = str(input("Deseja continuar [S/N] : "))
        
    if resposta in "Nn" :
        
        break
    
    
print(f"O numero de pessoas que são maiores de 18 anos é de {num_18}")
print(f"O numero de homens que foram cadastrados foi de  {num_homens}")
print(f"O numero de mulheres que são menores de 20 anos é de {num_mulhers_20}")