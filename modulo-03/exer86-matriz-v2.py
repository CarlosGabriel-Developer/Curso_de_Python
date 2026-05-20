matriz = []

for l in range(0,4) : 
    
    linhas = []
    
    for c in range(0,4) : 
        
        linhas.append(int(input(f"Digite um numero na posição [{l}][{c}]  ")))
        
    matriz.append(linhas[:])
    
print('-'*40)

for l in range(0,4) : 
    
    for c in range(0,4) :
        
        print(f"{matriz[l][c]:^5}", end=" ")
    print()
        
print('-'*40)
    
        
    