##Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.  

numero = int(input("Digite um numero : "))
razao = int(input("Qaul a razão : "))

termo = numero
contador = 1 

while contador <= 10 :
    
    print(f"{termo}", end="==>")
    
    termo += razao
    contador += 1
    
print("ACABOU")