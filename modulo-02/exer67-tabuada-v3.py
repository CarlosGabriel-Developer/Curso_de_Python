##Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

while True : 
    
    print("="*40)
    num = int(input("Quer ver a tabuada de qual valor : "))
    print("="*40)
    
    for i in range(1,11) :
        
        print(f"{num} X {i:2} = {num*i}")
    
     
    if num < 0 :
        break