##Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

user3 = int(input("Escolha um numero para sua tabuada : "))


for i in range(1,11,1):
    print(f"{user3} x {i} = {user3*i}")