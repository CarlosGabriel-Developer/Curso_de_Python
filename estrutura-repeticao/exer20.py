#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Digite um numero : "))

if num < 2 : 
    print("Esse numero não pode ser primo")
    
else : 
    primo = True
    print("Esse numero pode ser divisivel por esses outros numeros", end=" ")
    
    for i in range(2,num) : 
        
        if num % i == 0 : 
            primo = False
            print(i, end=",")

    print()
    
    if primo : 
        print("Esse numero é primo")
        
    else : 
        print("Esse numero não é primo")