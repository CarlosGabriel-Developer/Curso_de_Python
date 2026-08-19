##Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 


# Leitura do número N
n = int(input("Digite quantos elementos da sequência de Fibonacci deseja ver: "))

# Inicialização da sequência
a, b = 0, 1
cont = 0

# Loop para gerar os N primeiros elementos
while cont < n:
    print(a, end=' ')
    a, b = b, a + b  # Atualiza os valores de a e b
    cont += 1