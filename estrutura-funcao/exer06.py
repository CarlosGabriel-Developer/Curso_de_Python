#Faça um programa que converta a notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M.

# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.

# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas às vezes que desejar.

def converter(hora,minuto) : 
    
    if hora == 0 : 
        hora = 12 
        periodo = "A"
        
    elif hora < 12 :
        periodo = "A"
        
    elif hora == 12 :
        periodo = "P"
    
    else :
        hora -= 12
        periodo = "P"
        
    return hora,minuto,periodo

def mostrar(hora,minuto,periodo) :
    
    if periodo == "A" :
          print(f"{hora}:{minuto:02d} A.M.")
    else:
        print(f"{hora}:{minuto:02d} P.M.")


while True : 
    
    horas_atual = int(input('Horas Atual (0-23)'))
    minuto_atual = int(input('Minutos (0-59)'))
    
    hora, minuto, periodo = converter(horas_atual, minuto_atual)
    
    mostrar(hora, minuto, periodo)
    
    repetir = input("Deseja converter outro horário? (S/N): ").upper()

    if repetir != "S":
        print("Programa encerrado.")
        break