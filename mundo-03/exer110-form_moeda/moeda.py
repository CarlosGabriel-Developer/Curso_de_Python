def aumentar(moeda=0,taxa=0,formato=False): 
    resp = moeda + (moeda * taxa/100)
    return resp if formato is False else f"R$ {resp:.2f}"
       
def diminuir(moeda=0,taxa=0,formato=False):
    resp = moeda - (moeda*taxa/100)
    return resp if formato is False else f"R$ {resp:.2f}"

def dobro(moeda,formato=False):
    resp= moeda * 2
    return resp if formato is False else f"R$ {resp:.2f}"

    
def metade(moeda,formato=False):
    resp = moeda / 2
    return resp if formato is False else f"R$ {resp:.2f}"


def resumo(valor, taxa=0):
    print('-' * 30)
    print(f'{"RESUMO DE VALOR":^30}')
    print('-' * 30)

    print(f'Preço Analisado:\tR$ {valor:.2f}')
    print(f'Dobro do Preço :\t{dobro(valor,True)}')
    print(f'Metade do Preço:\t{metade(valor,True)}')
    print(f'{taxa}% de aumento: \t{aumentar(valor, taxa,True)}')
    print(f'{taxa}% de redução: \t{diminuir(valor, taxa,True)}')

    print('-' * 30)