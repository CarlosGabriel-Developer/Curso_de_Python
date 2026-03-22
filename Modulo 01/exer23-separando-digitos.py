import random

numero = random.randint(0, 9999)
n_str = str(numero)  
n = n_str.strip()    


print(n)
print(f"A unidade é {n[3]}")
print(f"Dezena é {n[2]}")
print(f"Centena é {n[1]}")
print(f"Milhar é {n[0]}")