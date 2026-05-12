## Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Qual o valor da casa ? : "))
salario = float(input("Qual é o seu salario atual : "))
anos = int(input("Em quantos anos vai pagar? : "))
mes = (anos *12)

prestacao = float(valor_casa / mes)

print(f"A sua prestação vai ser de {prestacao:.2f} por mes")

if prestacao > (salario*0.30) :
    print("Emprestimo negado")
    
else:
    print("Emprestimo aprovado")