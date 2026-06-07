#Faça um programa que calcule o mostre a média aritmética de N notas.
soma = contador = 0 

while True : 
     
    num = int(input("Digite um numero [00 para sair] : "))
    
    soma += num
    contador += 1
    
    if num == 00 :
        break

media = (soma / contador)

print(f"A soma dos numeros é igual {soma}")
print(f"A média apos a soma é igual {media}")