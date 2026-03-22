a = int(input("Digite um valor :"))
b = int(input("Digite um valor :"))
c = int(input("Digite um valor :"))
 

menor = a 
if b < a and b < c :
    menor = b
    
if c < a and c < b :
    menor = c
    
maior = c 
if a > b and a > c :
    maior = a 
    
if b > a and b > c :
    maior = b



print(f"""
O menor valor foi {menor}
O maior numero foi o {maior}""")

##[a,b,c]min(menor valor da lista), max(maior valor da lista)