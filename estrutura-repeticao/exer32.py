# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
# Código

n = int(input("Digite um número inteiro: "))

print(f"Números primos entre 1 e {n}:")

for num in range(2, n + 1):
    primo = True

    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            primo = False
            break

    if primo:
        print(num, end=" ")