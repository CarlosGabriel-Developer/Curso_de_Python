frase = "Curso em Video Python"

##fatiamento
print (frase[:9]) #mostra do inicio até nono index
print (frase[9:]) #inicia no nono index
print (frase[::3]) #inicia desde do inicio e pula de tres em tres

##analise
print (len(frase)) ##retorna numero de caracteres
print (frase.count("e")) ##conta quantas letras tal aparece
print (frase.count("o",0,13)) #conta quantas vezes aparece desse "Range" index 1 ate o 13
print (frase.find("deo")) #encontra o primeiro caracter escolhido
print ("Curso" in frase) #informa se tem tal palavra se encontra no texto

##transformação 
print(frase.replace("Python","ANDROID")) #transforma a primeira palavra 
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

##divisao
print(frase.split())

##juncao

print("--".join(frase))