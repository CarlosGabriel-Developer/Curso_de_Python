##Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

import random

lista_alunos = []

soma_altura = 0
media_altura = 0 


for i in range(30) : 
    
    idade_aluno = (random.randint(10,18))
    altura_aluno = (random.uniform(1.40,1.90))
    
    soma_altura += altura_aluno
    
    
    if idade_aluno > 13 and altura_aluno > media_altura: 
        
        lista_alunos.append(i)
        
print(f"Ao total foram {len(lista_alunos)} alunos maiores de 13 anos")
    