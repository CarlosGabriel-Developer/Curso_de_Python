

def fatorial (numero=1,show=0) :
    
    """Fatorial(Numero, show= False)
    
    --> Calcula o fatorial de um numero
    Para Numero:O numero a ser calculado
    Para Show:(opcional) Mostrar ou não contar
    Return: O valor fatorial do numero
    
    """
    
    f = 1
    
    for i in range(numero,0,-1):
        f*= i
    
    return f

numero = int(input('Numero: '))

print(fatorial(numero))