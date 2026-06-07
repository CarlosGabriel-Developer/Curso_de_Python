#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
soma = contador = 0

while True :
    
    idade = int(input("Digite a sua idade :[0 para sair]"))
    
    if idade < 0 : 
        break
    
    contador += 1
    soma += idade
    
print(f"A idade media do grupo é de {soma/contador:.2f}")