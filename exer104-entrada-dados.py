#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(num='') : 
    
    if num.isnumeric : 
        return f"Voce acabou de digita {num}"
    
    else : 
        
        return ('\033[31m Erro,Digite um numero válido]')




