def fatorial (num=0,show=True) : 
    
    f = 1 
    
    
    for i in range(num,0,-1) : 
        
        if show == True : 
            
            print(f'{i}', end=' ')
            
            if i > 1 : 
                
                print('X', end=' ')
                
            else : 
                print('=', end=' ')
                
                
        f*= i 
        
    return f


numero = int(input('Numero: '))

mostrar_numero = str(input('Mostrar os numeros [S/N]: ')).upper

if mostrar_numero == 'S' :
    show = True
    
else :
    show = False

print(fatorial(numero))

#==============================================


