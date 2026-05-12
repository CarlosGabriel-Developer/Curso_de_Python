##Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = int(input("Digite um numero [Digte 999 para parar o programa] : "))
num_digitados = soma_numeros = 0 

while num != 999 : 
    
    num_digitados += 1
    soma_numeros += num
    
    num = int(input("Digite um numero [Digte 999 para parar o programa] : ")) 
    
    
print(f"Você digitou {num_digitados} numeros")
print(f'A soma dos numeros digitados foi de {soma_numeros}')

    