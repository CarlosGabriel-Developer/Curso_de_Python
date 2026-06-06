#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.


num = int(input("Digite um numero : "))

if num < 2 :
    print("Esse numero não pode ser primo")
    
else : 
    primo = True
    
    for i in range(2,num) : 
        if num % i == 0 :
            primo = False
            break
        
    if primo :
        print("É um número primo.")
         
    else : 
        print("Não é um número primo.")