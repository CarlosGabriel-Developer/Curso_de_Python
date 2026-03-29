##Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.  

numero = int(input("Digite um numero : "))
razao = int(input("Qaul a razão : "))

termo0 = 0 
i = numero

while not termo0 == 11: 
    
    print(f"{i}", end="==>")
    
    termo0 += 1
    
print("ACABOU")