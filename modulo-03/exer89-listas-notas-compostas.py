##xercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


matriz = []

while True :


    nome_aluno = str(input("Digite o seu nome : ")).strip().capitalize()
    
    while True : 
            
        nota1_aluno = float(input("Digite a sua nota : "))
            
        if not 0 <= nota1_aluno <= 10 : 
                
            print("Valor invalidao, Tente novamente")
            
            continue
            
        nota2_aluno = float(input("Digite a sua nota : "))
        
        if not 0 <= nota2_aluno <= 10 : 
            
            print("Valor invalidao, Tente novamente")
            
            continue
        
        break
            
    media_aluno = (nota2_aluno + nota1_aluno) /2
    
    if media_aluno > 10 : 
        
        print("Média incorreta")
    
    matriz.append([nome_aluno,[nota1_aluno,nota2_aluno],media_aluno])
    
    user_aluno = str(input("Deseja continuar [S/N] : ")).strip().upper()
    
    if user_aluno in "N" : 
        
        break
    

print("-"*40)

print(f'{"N°":<5}{"NOME":<10}{"MEDIA":>10}')

print("-"*40)

for i,aluno in enumerate(matriz) : 
    
    print(f"{i:<4}{aluno[0]:<8}{aluno[2]:>12.1f}")

print("-"*40)


while True : 
    
    user_pesquisa = int(input("Deseja ver as notas dos alunos [999 para sair]"))
    
    if user_pesquisa <= len(matriz) -1 : 
        
        print(f"{matriz[user_pesquisa][0]} são {matriz[user_pesquisa][1]}")
        
    if user_pesquisa == 999 : 
        break
   
    
print("-- FIM --")