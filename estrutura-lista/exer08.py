#Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

banco_dados = []
alturas,idades = [],[]


for i in range(5) : 
    
    while True : 
        
        idade = int(input("Diga-me a sua idade : "))
        
        if idade > 120 : 
            print("Essa idade é invalida, por favor tente novamente")
        
        break
    
    while True : 
        
        altura = float(input("Agora a sua altura : "))
        
        if altura > 2.30 : 
            print("Essa altura é invalida, Tente novamente")
        
        break
    
    alturas.append(altura)
    idades.append(idade)
    

print("\n DADOS EM ORDEM INVERSA\n")

for i in range(4,-1,-1) :
    print(f"Idade: {idades[i]} | Altura: {alturas[i]}")