#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

num1 = num2 = 1
num_termo = int(input("Digite o numero de termos : "))

for i in range (num_termo) : 
    
    print(num1, end=" ")
    
    prox_num = num1 + num2
    
    num1 = num2
    
    num2 = prox_num