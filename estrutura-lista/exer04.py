#Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.


vogais = ['a','e','i','o','u']
contador = 0 

while True : 
    
    palavra = str(input("Digite uma palavra de até 10 caracteres : ")).lower().strip()

    if len(palavra) > 10 : 
        print("A palavra tem que ser menor ou igual a 10 caracters")
        continue

    for letra in palavra : 
        
        if letra not in vogais :
            print(letra,  end=" ") 
            contador += 1
            
    print()
    print(f"Essa palavra tem {contador} consoantes")