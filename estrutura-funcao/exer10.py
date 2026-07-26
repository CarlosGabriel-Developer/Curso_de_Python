#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mes_por_extenso de AAAA. Opcionalmente, valide a data e retorne None caso a data seja inválida.

def mes_por_extenso () : 

    meses = ['Janeiro','Fevereiro',"Março","Abril",'Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    
    data = input("Digite a data (DD/MM/AAAA): ")

    dia, mes, ano = data.split("/")

    print(f"{dia} de {meses[int(mes) - 1]} de {ano}")

        
mes_por_extenso()
    

        

    