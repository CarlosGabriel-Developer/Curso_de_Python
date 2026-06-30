##Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

#F - Feminino
#M - Masculino
#Sexo Inválido.

print("=== Exercício 03 === ")
genero = str(input("Sexo [M/F] : "))

print("-"*30)


if genero in "Mm" : 
    print("MASCULINO")
    
elif genero in "Ff" : 
    print("Femino")
    
else : 
    print("Invalido")