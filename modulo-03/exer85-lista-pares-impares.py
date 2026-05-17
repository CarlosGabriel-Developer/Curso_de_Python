##Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

principal = [[],[]]

for i in range(0,7,1) : 
    
    numero = (int(input(f"Digite um numero no index {i}: ")))
    

    if numero % 2 == 0 : 
        
        principal[0].append(numero)
        
    elif numero % 2 == 1 : 
        
        principal[1].append(numero)


print("="*40)   

print(f"Os valores pares digitados foram : {sorted(principal[0])}")

print(f"Os valores impares digitados foram : {sorted(principal[1])}")

print("="*40)

    