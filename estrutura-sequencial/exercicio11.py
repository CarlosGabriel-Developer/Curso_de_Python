##Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

#O produto do dobro do primeiro com metade do segundo .
#A soma do triplo do primeiro com o terceiro.
#O terceiro elevado ao cubo.



num1 = int(input("Digite um numero inteiro : "))

num2 = int(input("Digite um numero inteiro : "))

num3 = float(input("Digite um numero real : "))


print(f"O produto do dobro do primeiro com metade do segundo é igual \033[1;34m{(num1*2)+(num2/2):.2f}\033[0m")

print(f"A soma do triplo do primeiro com o terceiro é igual de \033[1;34m{(num1*3)+num3:.2f}\033[0m")

print(f"O terceiro elevado ao cubo é de \033[1;34m{num3**3:.2f}\033[0m")