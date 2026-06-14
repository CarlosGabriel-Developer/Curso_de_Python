#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

import random

maior = menor = 0 

while True : 
    
    soma = 0
    media = 0
    
    for i in range(30) : 
        
        num=input(random.randint(10,43))
        
        soma += num
        
    media = soma/30
        
    
    resposta = str(input("Deseja parar [S/n]"))
    
    if resposta in "Ss" : 
        break
    

print('A media')
print(media)
        
        