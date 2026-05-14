##Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista_num = []

while True : 
    
    numero = int(input('Digite um numero : '))
    lista_num.append(numero)
    
    print('Numero adicionado')
    
    user = str(input("Deseja continuar [S/N] ? ")).upper().strip()
    if user in 'Nn' : 
        break
    
sorted(lista_num)
    
print(f'Foram digitados {len(lista_num)} numero(s)')
print(f"A lista de numeros em ordem decrescente é {list(reversed(lista_num))}")
if lista_num in 5 : 
    
    print('O numero 5 foi digitado na lista')
    
else : 
    
    print('O numero 5 não foi digitado ha lista')
