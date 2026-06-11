##Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

import random

idades = []
alturas = []

# Gerando dados de 30 alunos
for i in range(30):
    idade = random.randint(10, 18)
    altura = round(random.uniform(1.40, 1.90), 2)

    idades.append(idade)
    alturas.append(altura)

# Calculando a média das alturas
media_altura = sum(alturas) / len(alturas)

# Contando alunos com mais de 13 anos e altura abaixo da média
contador = 0

for i in range(30):
    if idades[i] > 13 and alturas[i] < media_altura:
        contador += 1

print(f"Média das alturas: {media_altura:.2f} m")
print(f"Quantidade de alunos com mais de 13 anos e altura abaixo da média: {contador}")