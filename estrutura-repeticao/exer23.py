##Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

num_eleitores = int(input("Diga-me o numero total de eleitores : "))

carlos = 0 
gabriel = 0 
lunna = 0 

for i in range(num_eleitores) : 
    
    while True : 
        
        eleitor = int(input("Digite em quem pretende votar [carlos-1] ou [gabriel-2] ou [lunna-3]: "))
        
        if eleitor == 1 : 
            carlos += 1
            break
            
        elif eleitor == 2 : 
            gabriel += 1 
            break
        
        elif eleitor == lunna : 
            lunna += 1 
            break
        
        else :
            print("Incorreto, Tente novamente por favor")
            
print("\nResultado da eleição:")
print(f"Carlos: {carlos} votos")
print(f"Gabriel: {gabriel} votos")
print(f"Lunna: {lunna} votos")

if carlos > gabriel and carlos > lunna:
    print("Vencedor: Carlos")

elif gabriel > carlos and gabriel > lunna:
    print("Vencedor: Gabriel")

elif lunna > carlos and lunna > gabriel:
    print("Vencedor: Lunna")

else:
    print("Houve empate.")