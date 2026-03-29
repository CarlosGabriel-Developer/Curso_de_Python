##Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.


numero1 = int(input("Digite um numero : "))
numero2 = int(input("Digite um numero : "))

escolha = 0

while escolha !=  5 :
    
    print("==== MENU ====")
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos números")
    print("[ 5 ] sair do programa")
    print("=="*10)
    
    escolha = int(input("Escolha entre [1-5] : "))
    
    
    if escolha == 1 : 
        
        print(f"A soma dos valores {numero1} e {numero2} é de {numero1+numero2}")
        
    
    elif escolha == 2 : 
        
        print(f"A multiplicação dos valores {numero1} e {numero2} é de {numero1*numero2}")
        
    elif escolha == 3 : 
        
        maior = max(numero1,numero2)
        
        print(f"O maior entre os valores {numero1} e {numero2} é de {maior}")
        
    elif escolha == 4 : 
        
        print("== NOVOS NUMEROS ==")
        
        numero1 = int(input("Digite um numero NOVO: "))
        numero2 = int(input("Digite um numero NOVO: "))
        
    
    elif escolha == 5 : 
        
        print("== FIM DO PROGRAMA ==")
        
    
    else :
        
        print("Opção invalida")
        
print("=== FIM ===")
     

        
    
    