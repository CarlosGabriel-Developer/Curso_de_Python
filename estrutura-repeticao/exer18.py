#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True : 
    
    num = int(input("Digite um numero : "))

    resultado = 1 
    
    if 0 > num or num >= 15  : 
        
        print("Os numeros devem ser menores que 16 e maiores que 0")
        continue
        
    for i in range(1,num+1):
        
        resultado *= i
        
    print(resultado)
    
    usuario = str(input("Deseja continuar [S/n] : ")).lower()
    if usuario != 's' : 
        break