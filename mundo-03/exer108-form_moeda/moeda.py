def aumentar(moeda,taxa): 
    moeda = moeda + (moeda * taxa/100)
    return f"R$ {moeda:.2f}"
    
    
def diminuir(moeda,taxa):
    moeda = moeda - (moeda*taxa/100)
    return f"R$ {moeda:.2f}"

def dobro(moeda):
    moeda *= 2
    return f"R$ {moeda:.2f}"
    
def metade(moeda):
    moeda /= 2
    return f"R$ {moeda:.2f}"