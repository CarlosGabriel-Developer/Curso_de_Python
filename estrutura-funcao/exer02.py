# aça um programa para imprimir:

# 1
# 1   2
# 1   2   3
# .....
# 1   2   3   ...  n

# Para um n informado pelo usuário. Use uma função que receba um valor n inteiro, imprima até a n-ésima linha.


def teste (numero) : 
    
    for i in range (1,numero+1) : 
        for j in range (1,i+1) : 
            print(j, end=' ')
        print()
        
numeros = int (input('Numero que deseja : '))        
teste(numeros)