#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = menor = float(0) 

for i in range(0,5):
    
    peso = float(input(f"Peso de {i}º pesso : "))
    
    if menor < peso :
        peso = maior
    else :
        peso = menor
        
print(f"{menor}")
print(f"{maior}")