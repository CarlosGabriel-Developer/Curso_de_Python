##Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

##A) Quantas pessoas foram cadastradas.
##B) Uma listagem com as pessoas mais pesadas.
##C) Uma listagem com as pessoas mais leves.


banco_dados = []
pessoas = []
maior = menor = 0 

while True : 
    
    pessoas.append(str(input("Digite o seu nome  :")))
    
    pessoas.append(float(input("Digite o seu peso : ")))
    
    if len(banco_dados) == 0 : 
        
        maior = menor = pessoas[1]
        
    else : 
        
        if pessoas[1] < menor : 
            menor = pessoas[1]
            
        if pessoas[1] > maior :
            maior = pessoas[1]
            
             
    banco_dados.append(pessoas[:])
    pessoas.clear()
    
    usuario = str(input("Deseja continuar : [S/N]")).upper().strip()
    if usuario in "N" : 
        break
    
print("="*30)
print(banco_dados)
print("="*30)

print(f"Quantas pessoas foram cadastradas : {len(banco_dados)}")

print(f"Uma listagem com as pessoas mais pesadas {maior}")

print(f"Uma listagem com as pessoas mais leves {menor}")
