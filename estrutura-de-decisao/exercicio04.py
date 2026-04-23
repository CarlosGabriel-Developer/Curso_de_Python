##Exercício 04 Faça um programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra : ")).lower()

if letra.isalpha() and len(letra) == 1 : 
    
    if letra in "aeiou" : 
        print("E uma vogal")
    
    else : 
        print("É uma consoante")

else : 
    print("Por favor, digite apenas uma letra valida")