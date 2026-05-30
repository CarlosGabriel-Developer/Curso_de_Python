#Faça um programa que leia e valide as seguintes informações:

#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Estado Civil: 's', 'c', 'v', 'd';


while True : 
    
    nome = str(input("Digite o seu nome :")).strip().capitalize()
    
    if len(nome) < 3 : 
        
        print("Nome invalido, por favor tente novamente")
        continue

    idade = int(input("Digite a sua idade : "))
    
    if 0 >= idade >150 : 
        
        print("Idade com valor invalido.Por favor tente novamente")
        
    
