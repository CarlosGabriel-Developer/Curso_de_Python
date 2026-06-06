#Faça um programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
soma_nota = media_notas = 0 
for i in range(4) : 
    
    nota = (int(input("Digite a sua nota : ")))
    notas.append(nota)
    
    soma_nota += nota
    
media_notas = (soma_nota)/4

print(notas)
print(media_notas)