#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão


an = int(input("Qual é o termo que voce quer descobrir : "))

a1 = int(input("Qual é o primeiro termo : "))

n = int(input("Posição do termo : "))

r = int(input("Razão :"))



resultado = an=a1 + (n-1) * r

print(resultado)