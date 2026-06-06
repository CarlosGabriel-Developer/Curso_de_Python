#Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0


alunos = []


for i in range(10) :
    
    for l in range(4) : 
        alunos.append(float(input(f"Digite a sua nota do aluno[{i}][{l}]")))
        
        
print(alunos)