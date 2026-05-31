##Supondo que a população de um país A seja da ordem de 80_000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200_000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

a= 80000
b= 200000
numeros_anos = 0

while a <= b : 
    
    a *= 1.03
    b *= 1.015
    numeros_anos += 1
    
print('-'*80)
print(f'O numeros de habitantes depois de {numeros_anos} é de {a}')

print('-'*80)
print(f'O numeros de habitantes depois de {numeros_anos} é de {b}')
print('-'*80)
    
    