import random

nome1 = str(input("Nome do 1° aluno : "))
nome2 = str(input("Nome do 2º aluno : "))
nome3 = str(input("Nome do 3º aluno : "))
nome4 = str(input("Nome do 4º aluno : "))

lista = [nome1,nome2,nome3,nome4]
escolhido = random.choice(lista)

print(escolhido)