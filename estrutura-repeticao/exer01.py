#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


while True : 
    
    nota = int(input("Digite a sua nota entre 0 ate 10 : "))
     
    if 0 <= nota <= 10 : 
        break
    
    else : 
        print("Nota invalida,Tente novamente")
    
print(f"A sua nota é {nota}")
    
