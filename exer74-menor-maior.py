##Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


import random

num_tupla = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))

print(f"O menor valor : [{min(num_tupla)}]")

print(f"O maior valor : [{max(num_tupla)}]")

print(sorted(num_tupla))