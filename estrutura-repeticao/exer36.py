#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

num = int(input("Montar a tabuada de: "))
comeco = int(input("Começar por: "))
termina = int(input("Terminar em: "))

print(f"Vou montar a tabuada de {num} começando em {comeco} e terminando em {termina}")

for i in range(comeco, termina + 1):
    print(f"{num} X {i} = {num * i}")