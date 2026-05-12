
numero = int(input("Digte um numero : "))


az_num = (f"\033[1;34m{numero+1}\033[0m")

vm_num = (f"\033[1;31m{numero-1}\033[0m")

print(f"O seu numero é {numero} o seu antercessor é {vm_num} e o seu sucessor vai ser o {az_num}")
