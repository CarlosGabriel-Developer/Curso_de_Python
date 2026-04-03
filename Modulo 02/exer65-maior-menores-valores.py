##Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = int(input("Digite um numero : "))
soma = media = maior = menor = 0 

resposta = input("Deseja continuar [S/N] : ")

if resposta in "Ss" : 

    while resposta in "Ss" :
        
        soma += num
        media += 1 
        
        for i in num () : 
            
            if i == 1 : 
                
                maior = menor =  num 
                
            else : 
                
                if num > maior :
                    
                    maior = num
                    
                if num < menor : 
                    
                    menor = num 
                
        
else : 
    print("Fim do programa")
        