##Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.


palavra = str(input("Digite uma frase : ")).upper().strip().replace(" ", "")

palavra_reversa = palavra[::-1]



if palavra == palavra_reversa:
    print(f"A palavra {palavra} é igual á {palavra_reversa}")
    print("Essa palavra é um palindromo")
    
else:
    print(f"A palavra {palavra} não é igual á {palavra_reversa}")
    print("Essa palavra não é um palindromo")