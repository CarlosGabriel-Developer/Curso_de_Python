##Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

principal = []
pares = []
impares = []

while True : 
    
    principal.append(int(input('Digite um numero : ')))
    print('Numero adicionado')
    
    user = str(input('Deseja continuar '))
    if user in "Nn" : 
        break
    
    for i , v in enumerate(principal) : 
        
        if v % 2 == 0 : 
            pares.append(v)
            
        elif v % 2 == 1 : 
            impares.append(v)
    
    
    
print('== LISTAS DE NUMEROS == ')
print('Todos numeros digitados')
print(principal)

print('Todos os numeros pares')
print(pares)

print('Todos os numeros impares')
print(impares)