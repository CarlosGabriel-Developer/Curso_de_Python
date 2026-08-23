def aumentar(moeda,taxa,formato=False): 
    resp = moeda + (moeda * taxa/100)
    return resp if formato is False else f"R$ {resp:.2f}"
    
    
def diminuir(moeda,taxa,formato):
    resp = moeda - (moeda*taxa/100)
    return resp if formato is False else f"R$ {resp:.2f}"

def dobro(moeda,formato):
    resp= moeda * 2
    return resp if formato is False else f"R$ {resp:.2f}"
    
def metade(moeda,formato):
    resp = moeda / 2
    return resp if formato is False else f"R$ {resp:.2f}"