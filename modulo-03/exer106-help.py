##Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

while True:
    comando = input('\033[1;33mFunção ou Biblioteca > \033[m')

    if comando.upper() == 'FIM':
        break

    print('\033[1;34m')
    help(comando)
    print('\033[m')

print('\033[1;32mAté logo!\033[m')