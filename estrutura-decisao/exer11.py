#Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


perguta = int(input("Diga que dia é hoje  :(1-Domingo, 2- Segunda, etc.)"))

if perguta == 1 : 
    print("Domingo")
    
elif perguta == 2 : 
    print("Segunda")
    
elif perguta == 3 : 
    print("Terça")
    
elif perguta == 4 : 
    print("Quarta")
    
elif perguta == 5 : 
    print("Quinta")
    
elif perguta == 6 : 
    print("Sexta")
    
elif perguta == 7 : 
    print("Sabado")
    
else : 
    print("valor inválido")