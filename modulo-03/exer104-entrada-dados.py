#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(numero='') : 
    
    ok = False
    
    valor = 0
    
    while True : 
        
        num = str(input(numero))
        
        if num.isnumeric() : 
            valor = int(num)
            ok = True
            
        else : 
            print('\033[0;31mErro,Tente outro numero\033[m')
            
        if ok :
            break
        
    return valor

num = leiaInt("Digite um numero: ")

print(f"O numero digitado foi {num}")
            

