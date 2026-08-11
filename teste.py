
# def numero_maior (*numero): 
    
#     if len(numero) == 0 : 
#         print('Nenhum numero informado')
#         return
        
#     else : 
#         print(f'{len(numero)} numeros informados')
        
#     maior = numero[0]
    
#     for i in numero :
        
#         print(f'{i}', end=' ', flush=True)
        
#         if i > maior :
#             maior = i
            
#     print('O maior numero foi :')
#     print(f'{maior}')
         
# numero_maior()

import random
lista_numeros = []

def sortreio () : 
    
    lista_numeros.clear()

    for i in range(5):
        
        lista_numeros.append(random.randint(0,100))
        
    print('='*30)
    print('A lista dos numeros é de :')
    print(lista_numeros)
    print('='*30)
        
def soma_par() : 
    
    soma_numeros_pares = 0 
    contador_numero_pares = 0 
    
    for i in lista_numeros : 
        if i % 2 == 0 : 
            soma_numeros_pares += i 
            contador_numero_pares += 1 
            
    print(f'Foi informado {contador_numero_pares} numeros pares')
    print('='*30)
    print(f'A soma dos numeros pares é de {soma_numeros_pares}')
    print('='*30)
            

sortreio()
soma_par()