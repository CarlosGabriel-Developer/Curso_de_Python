##Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


lista_num = []

for i in range(0,5): 
    numero = int(input("Digite um numero : "))
    if i == 0 or numero > lista_num[-1] : 
        lista_num.append(numero)
        print('Adicionado no final da lista')
        
    else : 
        
        posicao = 0 
        
        while posicao < len(lista_num) : 
            if numero <= lista_num[posicao] : 
                lista_num.insert(posicao,numero)   
                print(f'Numero adicionado na posição {posicao} da lista')
                break
            posicao += 1     

print('LISTA DOS NUMEROS')
print(f'{lista_num}')