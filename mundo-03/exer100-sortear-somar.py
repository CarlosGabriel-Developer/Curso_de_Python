##Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
import random
lista_numeros = []

def sorteia() : 
    
    lista_numeros.clear()
    
    for i in range(5) : 
        
        lista_numeros.append(random.randint(0,100))
    
    print('='*30)
    print('A lista dos numeros é de :')
    print(lista_numeros)
    print('='*30)
    
sorteia()

def somaPar() : 
    
    soma_numerosPares = 0
    numeros_pares =0
    
    for i in lista_numeros : 
        
        if i % 2 == 0 : 
            
            numeros_pares +=1
            soma_numerosPares += i
            
    print(f'Foi informado {numeros_pares} numeros pares')
    print('='*30)
    print(f'A soma dos numeros pares é de {soma_numerosPares}')
    print('='*30)
    
sorteia()
sorteia()

somaPar()