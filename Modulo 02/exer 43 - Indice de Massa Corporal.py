#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#    IMC abaixo de 18,5: Abaixo do Peso
#    Entre 18,5 e 25: Peso Ideal
#    25 até 30: Sobrepeso
#    30 até 40: Obesidade
#    Acima de 40: Obesidade Mórbida

peso = float(input("Digite o seu peso : "))
altura = float(input("Digite a sua altura : "))

imc = peso /(altura**2)

print(f"Esse é o seu peso {peso}\nEssa é a sua altura {altura}")

if imc < 18.5:
    print(f"Seu imc é {imc}\nQuer dizer que você estar abaixo do peso")
    
elif imc < 25 : 
    print("Seu imc é {imc}\nQuer dizer que você estar PESO IDEAL")

elif imc < 30 : 
    print("Seu imc é {imc}\nQuer dizer que você estar PESO Sobrepeso")
    
elif imc < 40 : 
    print("Seu imc é {imc}\nQuer dizer que você estar PESO Obesidade")

else :
    print("Seu imc é {imc}\nQuer dizer que você estar PESO Obesidade Mórbida")