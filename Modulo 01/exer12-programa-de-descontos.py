produto = float(input("Digite o valor do produto : "))

desc = (produto - (produto *0.05))

print(f"Esse é o valor do produto {produto} e com um desconto de 5% {desc}")



print("==REVISÃO==")

print(f"Esse é o valor do produto \033[1;34m{produto}\033[0m e com um desconto de 5% \033[1;32m{desc}\033[0m")

