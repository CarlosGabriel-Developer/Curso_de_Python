##Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

num_cds = int(input("Digite o numero da sua coleção : "))

total_investido = 0

for i in range(num_cds):
    
    valor = float(input(f"Valor do cd [{i+1}] R$:"))
    total_investido += valor
    
media = total_investido/num_cds

print(f"\nValor total investido: R$ {total_investido:.2f}")
print(f"Valor médio gasto por CD: R$ {media:.2f}")