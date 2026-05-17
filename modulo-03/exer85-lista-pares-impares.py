##Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

principal = []

pares = []
impares = []


for i in range(0,7,1) : 
    
    principal.append(int(input(f"Digite um numero no index {i}: ")))
    
for i,v in enumerate(principal) : 
    
    if v % 2 == 0 : 
        
        pares.append(v)
        
    elif v % 2 == 1 : 
        
        impares.append(v)


print("="*40)   
print(sorted(principal))
print("="*40)

print(f"Os valores pares digitados foram : {sorted(pares)}")

print(f"Os valores impares digitados foram : {sorted(impares)}")
print("="*40)

    