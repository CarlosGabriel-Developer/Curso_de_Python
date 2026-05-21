##Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = []
soma_valores_pares = soma_valores_terceiracoluna = maior_valor_segundalinha = 0 

for l in range(0,3) : 
    
    linhas = []
    
    for c in range (0,3) : 
        
        linhas.append(int(input(f"Digite um numero na posição[{c}][{l}]")))
        
    matriz.append(linhas[:])
        
    linhas.clear()
 
print("-"*40)        
        
for l in range (0,3): 
    
    for c in range(0,3) : 
        
        print(f"{matriz[l][c]:^5}", end=" ")
        
    print()
    
print("-"*40)

for l in matriz :
    
    for v in l : 
        if v % 2 == 0 : 
            soma_valores_pares += v
    
        

    


print(f"A soma de todos os valores pares digitados foi de : {soma_valores_pares}")

print(f"A soma dos valores da terceira coluna foi de : {soma_valores_terceiracoluna}")
