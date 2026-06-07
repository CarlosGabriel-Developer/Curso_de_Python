#Faça um programa que peça as quatro notas de 4 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0


alunos = []


for i in range(4) : #alunos
    
    soma = media = 0 
    
    for l in range(4) : # notas
        
        while True :
             
            notas = (float(input(f"Digite a sua aluno[{i+1}] nota [{l+1}]")))
            
            if 0 < notas <= 10 :
                
                break
            
            print("Nota invalida,tente novamente")
        
        soma += notas
        
    media = soma/4
        
    alunos.append(media)
    
aprovados = 0

for a,n in enumerate(alunos): 
    
    if n > 7 : 
        print(f"O aluno {a+1} tem a média maior de {n}")
        aprovados += 1 
        
    else : 
        print("nenhum aluno tem a média acima de 7")

print(f"No final tivemos {aprovados} alunos aprovados")