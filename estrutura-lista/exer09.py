#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.


numeros = []
soma_quadrados = 0 

for i in range(10) : 
    
    while True : 
        
        numero = int(input(f"Digite numero {i+1}°"))
        numeros.append(numero)
        
        print('Numero adicionado')
        break
        
        
for i in numeros : 
     
    soma_quadrados += i ** 2 
    
    
print(f"A soma dos quadrados dos elementos do vetor é {soma_quadrados}")
    
        
    