#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os caracteres embaralhados. Por exemplo: se a função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

import random

def embaralha(msg): 
    
    lista = list(msg)
    random.shuffle(lista)
    return "".join(lista).capitalize()


print(embaralha('CARLOSGABRIELSOUSA'))