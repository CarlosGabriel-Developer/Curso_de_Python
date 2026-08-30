

try: 
    
    numero = int(input("Digte um numero : "))
    
except Exception as erro:
    print()
    print(f'O tipo de erro foi {erro}')
    print('Apenas numeros são validos')

else: 
    print(f"O seu numero é {numero} o seu antercessor é {numero-1} e o seu sucessor vai ser o {numero+1}")
