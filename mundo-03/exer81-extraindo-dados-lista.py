##Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.""
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []

while True : 
    
    numero = int(input('Digite um numero : '))
    numeros.append(numero)
    
    print('Número adicionado')
    
    user = str(input('Deseja continuar [S/N] : ')).strip().upper()
    
    if user == "N" :
        
        break
    
numeros.sort(reverse=True)


print(f'Foram digitados {len(numeros)} vezes')
print(f"A lista de valores, ordenada de forma decrescente {numeros}")

if 5 in numeros : 
    print('O numero 5 foi digitado na lista')

else:
    
        print('O numero 5 não foi digitado na lista')