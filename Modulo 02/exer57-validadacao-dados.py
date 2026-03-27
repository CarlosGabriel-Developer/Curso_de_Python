##Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = str(input("O sexo da pessoa é [M/F] : "))

while sexo not in "MmFf" : 
    
    print("Tente novamente")
    
    sexo = str(input("O sexo da pessoa é [M/F] : "))



if sexo in "Mm":
    
    print("=="*10)    
    print("BEM VINDO")
    print("=="*10)

    
elif sexo in "Ff":
    
    print("=="*10)    
    print("BEM VINDA")
    print("=="*10)
    