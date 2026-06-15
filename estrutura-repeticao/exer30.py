#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
maior = menor = None
soma = 0
num_tem = 0

while True:
    temperatura = float(input("Informe a temperatura [999 para sair]: "))

    if temperatura == 999:
        break

    soma += temperatura
    num_tem += 1

    if maior is None:
        maior = menor = temperatura
    else:
        if temperatura > maior:
            maior = temperatura

        if temperatura < menor:
            menor = temperatura

if num_tem > 0:
    media = soma / num_tem

    print(f"Maior temperatura: {maior}")
    print(f"Menor temperatura: {menor}")
    print(f"Média das temperaturas: {media:.2f}")
else:
    print("Nenhuma temperatura foi informada.")