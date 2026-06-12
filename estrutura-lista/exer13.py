#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

    # Mostre a quantidade de valores que foram lidos;
    # Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    # Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    # Calcule e mostre a soma dos valores;
    # Calcule e mostre a média dos valores;
    # Calcule e mostre a quantidade de valores acima da média calculada;
    # Calcule e mostre a quantidade de valores abaixo de sete;
    # Encerre o programa com uma mensagem;


numeros = []

while True : 
    
    numero = int(input("Digite um numero [-1 para sair]"))
    
    if numero == -1 : 
        break
    
    else : 
        numeros.append(numero)
    

print(f"Mostre a quantidade de valores que foram lidos {(len(numeros))}")

print("Exiba todos os valores na ordem em que foram informados, um ao lado do outro")

for i in numeros : 
    print(f"{i}", end=",")

print()

print("\nExiba todos os valores na ordem inversa à que foram informados, um abaixo do outro\n")

for i in reversed(numeros) : 
    
    print(f'{i}')



print('=== Isso é tudo pessoal ===')