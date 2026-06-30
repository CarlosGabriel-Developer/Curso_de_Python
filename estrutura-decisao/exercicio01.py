##Faça um programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite um numero : [1-10]"))
num2 = int(input("Digite outro numero : [1-10]"))

if num1 > num2 :
    
    print("Numero 1 escolhido foi o {num1}, ele é maior que o segundo numero escolhido")
    
elif num2 > num1 :
    
    print("Numero 2 escolhido foi o {num2}, ele é maior que o primeiro numero escolhido")
    
else : 
    
    print("Ambos os numeros são iguais")