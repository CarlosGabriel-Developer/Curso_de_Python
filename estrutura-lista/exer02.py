#Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

for i in range(10):
    
    num = int(input("Digite um numero : "))
    #lista.apped(int(input))
    lista.append(num)
    
print(lista[::-1])