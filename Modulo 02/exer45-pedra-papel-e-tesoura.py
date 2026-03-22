import random


print("""
OPCÂOES
[0] PEDRA
[1] PAPEL
[2] TESOURA""")

computador = random.randint(0,2)
jogador = int(input("Qual serár a sua escolha : "))

if jogador == 0 : 
    
    if computador == 0 :
        print('== EMPARTE ==')
    elif computador == 1 : 
        print("== JOGADOR PERDEU == ")
        print("== COMPUTADOR VENCEU == ")
    elif computador == 2 :
        print("== JOGADOR VENCEU ==")
        print("== COMPUTADOR PERDEU == ")
        
    print(f"A Escolha do jogador foi {jogador}")
    print(f"A escolha do computador foi {computador}")



elif jogador == 1 : 
    
    if computador == 0 :
        print("== JOGADOR VENCEU ==")
        print("== COMPUTADOR PERDEU == ")

    elif computador == 2 :
        print("== JOGADOR PERDEU == ")
        print("== COMPUTADOR VENCEU == ")
        
    else:    
        print('== EMPARTE ==')
        
    print(f"A Escolha do jogador foi {jogador}")
    print(f"A escolha do computador foi {computador}")    
        
elif jogador == 2 : 
    
    if computador == 0 :
        print("== JOGADOR PERDEU == ")
        print("== COMPUTADOR VENCEU == ")
        
    elif computador == 1 :
        print("== JOGADOR VENCEU ==")
        print("== COMPUTADOR PERDEU == ")
        
    else :
        print('== EMPARTE ==')
        
    print(f"A Escolha do jogador foi {jogador}")
    print(f"A escolha do computador foi {computador}")    
        
else  :
    print("Opção invalida")
            
    
        
        