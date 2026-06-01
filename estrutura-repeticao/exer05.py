##Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.


while True:

    a = int(input("Digite a população do país A: "))
    b = int(input("Digite a população do país B: "))

    while a <= 0 or b <= 0:
        print("As populações devem ser maiores que zero.")
        a = int(input("Digite a população do país A: "))
        b = int(input("Digite a população do país B: "))

    taxa_a = float(input("Digite a taxa de crescimento do país A (%): "))
    taxa_b = float(input("Digite a taxa de crescimento do país B (%): "))

    while taxa_a <= 0 or taxa_b <= 0:
        print("As taxas devem ser maiores que zero.")
        taxa_a = float(input("Digite a taxa de crescimento do país A (%): "))
        taxa_b = float(input("Digite a taxa de crescimento do país B (%): "))

    anos = 0

    while a < b:
        a *= (1 + taxa_a / 100)
        b *= (1 + taxa_b / 100)
        anos += 1

    print(f"Serão necessários {anos} anos para que A alcance ou ultrapasse B.")

    resposta = input("Deseja realizar outro cálculo? (S/N): ").strip().upper()

    if resposta != "S":
        break