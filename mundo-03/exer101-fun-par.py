def par(num=0) : 
    
    if num % 2 == 0 : 
        
        return True
    
    else: 
        return False
    
print(par(322))

numero = int(input('Numero: '))

if par(numero) : 
    print("È par")
else : 
    print('Não é par')

print(par(numero))