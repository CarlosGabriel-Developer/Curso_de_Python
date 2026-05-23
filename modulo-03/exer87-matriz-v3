####Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = []

soma_valores_pares = soma_terceira_coluna = maior_valor_segunda_linha = 0 

for linha in range (0,3) : 
    
    linhas = []
    
    for coluna in range(0,3) : 
        
        linhas.append(int(input(f"Digite um numero na posição [{linha}][{coluna}]")))
        
    matriz.append(linhas[:])
    
    linhas.clear()
    
print("-"*40)

for linha in range(0,3) : 
    
    for coluna in range(0,3):
        
        print(f"{matriz[linha][coluna]:^5}", end=" ")
        
    print()
    
print("-"*40)

for linhas in matriz : 
    
    for i in linhas : 
        if i % 2 == 0 :
            soma_valores_pares += i
            
    soma_terceira_coluna += linhas[2]
    
    maior_valor_segunda_linha = max(matriz[1])
    
    

print(f"A soma de todos os valores pares digitados foram : {soma_valores_pares}")
print(f"A soma dos valores da terceira coluna : {soma_terceira_coluna}")
print(f"O maior valor da segunda linha {maior_valor_segunda_linha}")
print("-"*40)