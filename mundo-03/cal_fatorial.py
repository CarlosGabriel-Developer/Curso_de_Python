

def fatorial(num) : 
    
    f = 1
    
    for i in range(1,num+1) : 
        f *= i
        
    return f

numero = int(input("Numero: "))

fat = fatorial(numero)

print(f'O fatorial do numero {numero} é de {fat}')