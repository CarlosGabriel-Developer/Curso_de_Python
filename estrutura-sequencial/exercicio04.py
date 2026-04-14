##Faça um programa que peça as 4 notas bimestrais e mostre a média. 

soma = 0 

for i in range(1,5,1):
    
    nota = float(input("Nota {i} : "))
    soma += nota
    
print(f"A media das notas é igual {soma/4}")