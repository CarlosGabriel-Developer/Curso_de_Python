##Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

principal = []
pares = []
impares = []

while True : 
    
    numero = int(input('Digite um numero : '))
    principal.append(numero)
    
    print('Numero adicionado')
    
    if numero % 2 == 0 : 
        
        pares.append(numero)
        
    else : 
        
        impares.append(numero)
    
    user = str(input('Deseja continuar '))
    if user in "Nn" : 
        break
    
print('== LISTAS DE NUMEROS == ')
print('Todos numeros digitados')
print(principal)

print('Todos os numeros pares')
print(pares)

print('Todos os numeros impares')
print(impares)