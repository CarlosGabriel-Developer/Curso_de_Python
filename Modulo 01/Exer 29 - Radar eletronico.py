carro = float(input("Qual a velocidade :"))

if carro <= 80 :
    print("Você não foi multado")
    
else:
    print("Vocẽ foi multado")
    
    multa = (7.00*(carro-80))
    
    print(f"Valor da multa é {multa}")