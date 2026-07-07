#Uma academia deseja fazer um censo entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
soma_alturas = 0
soma_pesos = 0
quantidade = 0

while True:
    codigo = int(input("Código do cliente (0 para encerrar): "))

    if codigo == 0:
        break

    altura = float(input("Altura (m): "))
    peso = float(input("Peso (kg): "))

    # Primeiro cliente
    if quantidade == 0:
        maior_altura = menor_altura = altura
        codigo_maior = codigo_menor = codigo

        maior_peso = menor_peso = peso
        codigo_gordo = codigo_magro = codigo

    # Cliente mais alto
    if altura > maior_altura:
        maior_altura = altura
        codigo_maior = codigo

    # Cliente mais baixo
    if altura < menor_altura:
        menor_altura = altura
        codigo_menor = codigo

    # Cliente mais gordo
    if peso > maior_peso:
        maior_peso = peso
        codigo_gordo = codigo

    # Cliente mais magro
    if peso < menor_peso:
        menor_peso = peso
        codigo_magro = codigo

    soma_alturas += altura
    soma_pesos += peso
    quantidade += 1

if quantidade > 0:
    media_altura = soma_alturas / quantidade
    media_peso = soma_pesos / quantidade

    print(f"\nCliente mais alto: código {codigo_maior}, altura {maior_altura:.2f} m")
    print(f"Cliente mais baixo: código {codigo_menor}, altura {menor_altura:.2f} m")
    print(f"Cliente mais gordo: código {codigo_gordo}, peso {maior_peso:.1f} kg")
    print(f"Cliente mais magro: código {codigo_magro}, peso {menor_peso:.1f} kg")
    print(f"Média das alturas: {media_altura:.2f} m")
    print(f"Média dos pesos: {media_peso:.1f} kg")
else:
    print("Nenhum cliente foi cadastrado.")