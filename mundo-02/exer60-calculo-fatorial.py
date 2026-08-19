##Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.


numero = int(input("Digite um numero que serar fatoriado : "))

i = numero
f = 1 

while i > 0: 
    
    print(f"{i}", end=" ")
    print(" X " if  i > 1 else "=", end=" " ) 
    
    f *= i
    i -= 1 
    
    
    
print(f"O fatorial do numero {f}")
