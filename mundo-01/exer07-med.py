try: 

    nota1 = float(input("Digite a sua primeira nota :"))
    nota2 = float(input("Digite a sua segunda nota :"))
    
except : 
    print('Apenas numeros validos')
    
else:
    media = (nota2 + nota1) / 2
    print(f'A media da nota do aluno é {media}')