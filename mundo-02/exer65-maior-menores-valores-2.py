respota = "s"

soma = quatidade = media = maior = menor = 0 

while respota in "Ss" :
    
    num = int(input("Digite um numero : "))
    soma += num
    quatidade += 1 
    
    if quatidade == 1 :
        
        maior = menor = num
        
    else :
        
        if num > maior :
            
            maior = num
            
        if num < menor :
            
            menor = num 
            
    respota = str(input("Quer continuar ? [S/N]")).upper().strip()[0]
    
media = soma / quatidade
