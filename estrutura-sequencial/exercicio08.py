##Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Quanto você ganha por hora : "))

numero_horas = int(input("Quantas horas trabalhadas no mês : "))

total_salario = numero_horas * valor_hora 

print(f"O valor da hora trabalhada é de {valor_hora}")
print(f"O numero de horas trabalhada é de {numero_horas}")

print(f"E o valor do sálario é de {total_salario}")