frase = str(input("Digite uma frase : ")).strip().upper()

contador  = frase.count("A")

print(f"""
      A sua frase é {frase}
      Quantas vezes a letra A, aparece é de {contador} vezes 
      
      A posição que ela aparece pela primeira vez foi na posição : {frase.find("A")+1}
      
      A posição que ela aparece pela ultima vez foi na posição : {frase.rfind("A")+1}
      
      
      """)
