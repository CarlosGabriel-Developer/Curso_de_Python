salario_antigo = float(input("DIgite o seu salario atual : "))

if salario_antigo < 1250 :
    salario_novo = (salario_antigo + (salario_antigo*0.15))
    
    print(f"Esse é o seu novo salario atual {salario_novo}")
    
if salario_antigo >= 1250 : 
    salario_novo = (salario_antigo + (salario_antigo*0.10))
    
    print(f"Esse é o seu novo salario atual {salario_novo}")
    
    

    
    