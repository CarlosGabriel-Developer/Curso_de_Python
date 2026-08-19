##Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input("Digite a expressão : ")).strip()

lista = []

for i in exp : 
    
    if i == "(" : 
        lista.append("(")
        
    elif i == ")" : 
        
        if len(lista) > 0 : 
             
             lista.pop()
             
        else : 
            
            lista.append(')')
            break 



print("=="*20)

if len(lista) == 0 : 
    print("Sua expressão está correta")

else : 
    print("Sua expressão não está correta")
    
print("=="*20)