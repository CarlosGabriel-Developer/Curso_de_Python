def funcao() : 
    num = 4
    print(f'Numero tem o valor de {num}')
    
    
num = 10

funcao()

print(f'Numero fora do escopo {num}')


print('='*30)

def teste (b) : 
    global a
    a = 8
    b += 4
    c = 4
    
    print(f'O valor de {a}')
    print(f'O valor de {b}')
    print(f'O valor de {c}')


a = 5 
teste(a)
print(f'A fora do espoco {a}')

print('='*30)

def soma(a=0,b=0,c=0) :
    
    Soma = a+b+c
    return Soma

resp1 = soma(4,5,8)
resp2 = soma(8,4)
resp3 = soma(4)

print(f'A soma dos calculos deram {resp1},{resp2},{resp3}')