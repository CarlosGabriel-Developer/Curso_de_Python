##Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

#Para Megabytes: Gigabytes * 1024
#Para Kilobytes: Gigabytes * 1024 * 1024

#Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.



Gigabytes = int(input("Gigabytes : "))

Megabytes = Gigabytes * 1024

Kilobytes = Gigabytes * 1024 * 1024

print(f"Gigabytes : {Gigabytes}")
print(f"Megabytes : {Megabytes}")
print(f"Kilobytes : {Kilobytes}")