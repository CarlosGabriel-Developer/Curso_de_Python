##Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

import random

soma_alunos = 0

num_turmas = random.randint(1,6)

for i in range(num_turmas) : 
    
    num_alunos = random.randint(35,40)
    print(f"A sala {i+1} tem esse numero de alunos {num_alunos}")
    soma_alunos += num_alunos

media_num = soma_alunos/num_turmas



print(f"A média do alunos nas {num_turmas} salas é de {media_num:.2f}")