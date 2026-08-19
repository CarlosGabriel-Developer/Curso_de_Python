def fatorial (num=1) : 
    
    f =1
    
    for i in range(num,0,-1): 
        f *= i
        
    return f

# f1 = fatorial(87)
# f2 = fatorial(7)
# f3 = fatorial(40)

n = int(input('Numero: '))
print(f'O fatorial de {n} é {fatorial(n)}')

# print(f'O fatorial de é {f1}')
# print(f'O fatorial de é {f2}')
# print(f'O fatorial de é {f3}')