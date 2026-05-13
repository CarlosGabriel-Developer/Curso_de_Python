##Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 


lista_num = []

while True : 
    
    num = int(input("Digite um numero : "))
        
    if num not in lista_num :
        lista_num.append(num)
        
    else : 
        print('Numero já digitado.Tente outro numero')
        
    user = str(input("Deseja continuar [S/N] ? : ")).upper().strip()

    if user == "N" : 
        break
    
print('='*40)    
print("LISTA DE NUMEROS DIGITADOS") 
print('='*40)    
print(sorted(lista_num))