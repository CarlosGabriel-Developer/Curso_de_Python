##xercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


matriz_main = []
alunos = []


while True :
    
    while True:
        
        nome_aluno = str(input("Digite o seu nome :")).strip().capitalize()
        notas1 = float(input("Digite a sua nota : "))
        notas2 = float(input("Digite a segunda nota : "))
        
        usuario = str(input("Deseja continuar [S/N] : "))
        
        if usuario in "Nn" :
            break
        
    print("-"*40)
        
    usuario = str(input("Deseja continuar [S/N] : "))
        
    if usuario in "Nn" :
        break
            
    print("-"*40)
        
print("Ate a proxima ")