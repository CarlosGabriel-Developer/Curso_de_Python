#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#    EQUILÁTERO: todos os lados iguais
#    ISÓSCELES: dois lados iguais, um diferente
#    ESCALENO: todos os lados diferentes

linha1 = int(input("Primeiro Segmento : "))
linha2 = int(input("Segundo segmento : "))
linha3 = int(input("Terceiro segmentos :"))

if (linha1+linha2>linha3) and (linha2+linha3>linha1) and (linha3+linha1>linha2) : 
     

    print("PODEMOS FORMAR UM TRIÂNGULO")

    if(linha1 == linha2 == linha3) :
        print("Triângulo Equilátero serar formado")
        
    elif(linha1 != linha2 != linha3 != linha1):
        print("Triângulo Escaleno serar formado")
        
    else:
        print("Triângulo Isosceles serar formado")
   
   
else:
    print("NÃO PODEMOS FORMAR UM TRIÂNGULO")    
    