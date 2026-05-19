##Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.


matriz = []
teste = []


for c in range (0,3,1) : 
    
    for l in range(0,3,1) : 
        
        teste.append(int(input(f"Digite um numero na posição [{c}] [{l}] : ")))
        matriz.append(teste[:])
        teste.clear()


print("="*40)
for l in range(0,3,1) : 
    
    for c in range(0,3,1) : 
        print(f"{matriz[l][c]}", end=" ")
    
    
    
print("="*40)