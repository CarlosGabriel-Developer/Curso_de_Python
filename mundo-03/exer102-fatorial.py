

def fatorial (numero=1,show=True) :
    
    """Fatorial(Numero, show= False)
    
    --> Calcula o fatorial de um numero
    Para Numero:O numero a ser calculado
    Para Show:(opcional) Mostrar ou não contar
    Return: O valor fatorial do numero
    
    """
    
    f = 1
    
    for i in range(numero,0,-1):
        
        if show == True : 
            print(i, end=' ')
            if i > 1 : 
                print('X',end=' ') 
                
            else : 
                print('=', end=' ')
        f*= i
    
    return f

numero = int(input('Numero: '))

print(fatorial(numero))