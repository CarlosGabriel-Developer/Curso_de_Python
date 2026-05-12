##Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


num = contador = soma = 0 

while True :
    
    num = int(input("DIGITE UM NUMERO : [999 PARA SAIR]"))
    
    
    if num == 999 : 
        
        break
    
    else : 
        contador += 1
        soma += num
    
    
    
    
print(f"DIGITOU {contador} NUMEROS")
print(f"A SOMA DOS NUMEROS DIGITADOS {soma}")
    