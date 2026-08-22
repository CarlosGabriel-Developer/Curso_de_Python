def aumentar(moeda,taxa): 
    moeda = moeda + (moeda * taxa/100)
    return moeda
    
    
def diminuir(moeda,taxa):
    moeda = moeda - (moeda*taxa/100)
    return moeda

def dobro(moeda):
    moeda *= 2
    return moeda
    
def metade(moeda):
    moeda /= 2
    return moeda