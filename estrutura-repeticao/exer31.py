# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input("Digite um numero: "))

if num < 2:
    print("Esse numero não pode ser primo")

else:
    primo = True

    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print("Esse numero é primo")
    else:
        print("Esse numero não é primo")