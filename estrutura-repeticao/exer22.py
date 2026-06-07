#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
soma = contador = 0

while True :
    
    idade = int(input("Digite a sua idade :[Um numero abaixo de zero para sair]"))
    
    if idade > 120 : 
        print("Idade invalida, Tente novamente por favor")
        continue
    
    if idade < 0 : 
        break
    
    contador += 1
    soma += idade
    
media = soma / contador

if  25 >= media >= 0 : 
    status = "jovens"

elif 59 >= media >= 26 :
    status = "adultos"
    
else : 
    status ="idosos" 

print(f"A idade media do grupo é de {media:.2f}")
print(f"È um grupo de {status}")