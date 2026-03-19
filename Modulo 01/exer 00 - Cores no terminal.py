texto = str("carlos gabriel sousa")

print(texto)

print(f'\033[30m{texto}') #fonte branco
print(f'\033[31m{texto}') #fonte vermelha
print(f'\033[32m{texto}') #fonte verde
print(f'\033[33m{texto}') #fonte amarela
print(f'\033[34m{texto}') #fonte azul
print(f'\033[35m{texto}') #fonte roxo
print(f'\033[36m{texto}') #fonte ciano
print(f'\033[37m{texto}') #fonte cinza


print(f'\033[1;34m{texto}') #a fonte fica em negrito
print(f'\033[7;34m{texto}') #a fonte fica em negativo
print(f'\033[4;34m{texto}') #a fonte fica em negativo e undeline


print(f'\033[0;31;46m{texto}')