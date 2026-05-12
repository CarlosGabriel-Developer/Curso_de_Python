##Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador_numeros = soma_numeros = numero_maior = numero_menor = 0 


numero = int(input("Digite um numero : "))

resposta = input("Deseja continuar [S/N] : ").upper().strip()

contador_numeros += 1 
soma_numeros += numero

while resposta in "Ss" : 
    
    if numero > numero_maior : 
        
        numero_maior = numero
    
    elif numero  < numero_menor : 
        
        numero_menor = numero
        
    
    numero = int(input("Digite um numero : "))

    contador_numeros += 1 
    soma_numeros += numero

    resposta = input("Deseja continuar [S/N] : ").upper().strip()
        
        
                
print("Fim do programa")
print(f"Você digitou {contador_numeros} numeros")
print(f"A soma dos numeros é de {soma_numeros}")
print(f"A media dos numeros é de {soma_numeros/contador_numeros}")
    