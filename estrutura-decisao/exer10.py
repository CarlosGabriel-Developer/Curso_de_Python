##Faça um programa que pergunte em que turno você estuda. Peça para digitar:

#     M - Matutino
#     V - Vespertino
#     N - Noturno.

# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


perguta = str(input("Em qual horario você estuda [M/V/N]: "))

if perguta == "M" : 
    print("Bom Dia")
    
elif perguta == "V" : 
    print("Boa Tarde")
    
elif perguta == "N" : 
    print("Boa Noite")
    
else : 
    print('Valor Inválido!')