# ##Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como Inocente". 

suspeito = []

pistas = 0

while True : 
    
    perguta1 = str(input("Telefonou para a vítima? [s/n]")).strip().lower()
    
    if perguta1 in "Ss" : 
        pistas += 1 
        
    perguta2 = str(input("Esteve no local do crime [s/n]")).strip().lower()
    
    if perguta2 in "Ss" : 
        pistas += 1 
        
    perguta3 = str(input("Mora perto da vítima [s/n]")).strip().lower()
    
    if perguta3 in "Ss" : 
        pistas += 1 
        
    perguta4 = str(input('Devia para a vítima [s/n]')).strip().lower()
    
    if perguta4 in "Ss" : 
        pistas += 1
         
    perguta5 = str(input("Já trabalhou com a vítima[s/n]")).strip().lower()
    
    if perguta5 in "Ss" : 
        pistas += 1 
        
    break

if pistas > 5 : 
    
    print("Você é o assasino")

elif 4 >= pistas >= 3 : 
    
    print("Você é Cúmplice ")