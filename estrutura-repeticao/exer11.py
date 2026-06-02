##Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Digite um numero : "))
num2 = int(input("Digite outro numero : "))

inicio = min(num1,num2)
final = max(num1,num2)
soma = 0 

for i in range(inicio,final) : 
    
    print(i, end=" ")
    soma += i
   
   
print() 
print(f"A soma dos numero é {soma}")