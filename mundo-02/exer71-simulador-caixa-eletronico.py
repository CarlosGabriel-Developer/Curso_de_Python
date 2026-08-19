##Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

user_origin = int(input("Qual será o valor a ser sacado: "))

total = user_origin
cel = 50
total_cel = 0

while True:
    
    if total >= cel:  # aqui corrige a lógica principal
        total -= cel
        total_cel += 1
        
    else:
        if total_cel > 0:
            print(f"O total {total_cel} de cédulas de R$ {cel}")
        
        # troca de cédula (corrigido = em vez de ==)
        if cel == 50:
            cel = 20
        elif cel == 20:
            cel = 10
        elif cel == 10:
            cel = 1
        
        total_cel = 0  # corrigido (sem :)
        
        if total == 0:
            break