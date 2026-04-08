numero = int(input("Digite um numero : "))

print(f"O seu numero é {numero}")
print(f"O dobro do seu numero é {numero*2}")
print(f"O tribloe do seu numero é {numero*3}")
print(f"A raiz quadrada do seu numero é {numero**0.5:.2f}")

print("===REVISÃO===")
print(f"O seu numero é\033[1;32m {numero}\033[0m")
print(f"O dobro do seu numero é\033[1;32m {numero*2}\033[0m")