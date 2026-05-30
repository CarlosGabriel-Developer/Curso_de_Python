##Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True : 
    
    nome = str(input("Digite o seu nome : ")).strip().upper()
    
    senha = str(input("Digite a sua senha :")).strip()
    
    if senha.upper() == nome.upper() :
        
        print("A senha não pode ser igual ao seu nome,Tente novamente")
        
    else : 
        
        break
    
print(f"Esse é o seu nome {nome.capitalize()}\nE essa é a sua senha {senha}")