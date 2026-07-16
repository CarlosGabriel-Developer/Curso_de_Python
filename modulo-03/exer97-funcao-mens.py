#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msn):

    print("-" * len(msn))
    print(msn)
    print("-" * len(msn))



usuario = str(input('MSN : '))

escreva(usuario)

escreva("Curso em Video")
escreva('Lunna')