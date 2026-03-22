#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um numero : "))

print("""
Base de conversão
[1] - BINÁRIO
[2] - OCTAL
[3] - HEXADECIMAL""")

escolha = int(input("Faça sua escolha [1-3] : "))

if escolha == 1 :
    print(f'Binário : {bin(num)[2:]}')
    
elif escolha == 2 : 
    print(f"OCTAL : {oct(num)[2:]}")
    
elif escolha == 3 :
    print(f"Hexadecimal : {hex(num)[2:]}")

else :
    print("Numero invalido tente novamente")