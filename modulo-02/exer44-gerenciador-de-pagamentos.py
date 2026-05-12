#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#    à vista dinheiro/cheque: 10% de desconto
#    à vista no cartão: 5% de desconto
#    em até 2x no cartão: preço formal
#    3x ou mais no cartão: 20% de juros


print("++== LOJA ==++")
valor = float(input("Preço das compras : "))

print("""
FORMAS DE PAGAMENTO
[1] A VISTA DINHEIRO/CHEQUE
[2] A VISTA CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO""")

opcao = int(input("Escolha uma opção : "))

if opcao == 1 :
    print(f"A sua compra de R${valor} vai custar R${valor-(valor * 0.10)} no final ")
    
elif opcao == 2 :
    print(f"A sua compra de R${valor} vai custar R${valor-(valor * 0.05)} no final ")
    
elif opcao == 3 :
    print(f"A sua compra é de R${valor} sem juros")
    print(f"Serar dividido em 2x vezes de {valor/2}")
    
elif opcao == 4 :
    num_parcelas = int(input("Quantas parcelas :"))
    valor_total = (valor+(valor*.20))
    valor_parcela = (valor+(valor*0.20))/num_parcelas
    
    print(f"Serar dividido em X{num_parcelas} vezes no valor de {valor_parcela}\ne o valor total a se pagar é de {valor_total}")
    
else:
    print("Invalido tente novamente")