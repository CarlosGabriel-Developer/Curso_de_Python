distancia = float(input("Qual a distancia da viagem :"))


if distancia >= 200:
    
    preco = ((0.50 * distancia))
    
    print(f"O custo foi de {preco}")
    
else:
    
    preco = ((0.45 * distancia))
    
    print(f"O custo da viagem foi {preco}")