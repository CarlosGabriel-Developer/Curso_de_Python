##Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

area = float(input("Digite o tamanho da área em m²: "))

# litros necessários com 10% de folga
litros_necessarios = (area / 6) * 1.1

# --- Apenas latas ---
latas = math.ceil(litros_necessarios / 18)
preco_latas = latas * 80

# --- Apenas galões ---
galoes = math.ceil(litros_necessarios / 3.6)
preco_galoes = galoes * 25

# --- Mistura ---
latas_mistura = int(litros_necessarios // 18)
resto = litros_necessarios - (latas_mistura * 18)

galoes_mistura = math.ceil(resto / 3.6)

preco_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

# --- Resultados ---
print("\n=== RESULTADOS ===")

print(f"\nApenas latas:")
print(f"{latas} lata(s) - R$ {preco_latas:.2f}")

print(f"\nApenas galões:")
print(f"{galoes} galão(ões) - R$ {preco_galoes:.2f}")

print(f"\nMistura:")
print(f"{latas_mistura} lata(s) e {galoes_mistura} galão(ões) - R$ {preco_mistura:.2f}")