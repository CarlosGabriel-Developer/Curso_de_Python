##Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

user = int(input("Escolha um numero para ver sua tabuada : "))



print("=== TABUADA ===")
print("="*15)

for i in range(1,11,1):
    print(f"{user} x {i:2} = {user*i}")
    
print("="*15)