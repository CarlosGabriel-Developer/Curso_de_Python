#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def funcao (num): 

    return len(str(num))

numero = int(input('Digite um numero: '))

print(f'O numero tem {funcao(numero)} digitados')