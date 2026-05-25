##xercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


matriz = []
<<<<<<< HEAD


=======

while True :


    nome_aluno = str(input("Digite o seu nome : ")).strip().capitalize()
    
    not1_aluno = float(input("Digite a primeira nota : "))
    
    not2_aluno = float(input("Digite a segunda nota : "))
    
    media_aluno = not2_aluno + not1_aluno /2
    
    matriz.append([nome_aluno,[not1_aluno,not2_aluno],media_aluno])
    
    user_aluno = str(input("Deseja continuar [S/N] : ")).strip().upper()
    
    if user_aluno in "N" : 
        
        break
    

print("-"*40)

print(f'{"N°":<5}{"NOME":<10}{"MEDIA":>10}')

print("-"*40)

for i,aluno in enumerate(matriz) : 
    
    print(f"{i:<4}{aluno[0]:<8}{aluno[2]:>12.1f}")

print("-"*40)

>>>>>>> refactor
