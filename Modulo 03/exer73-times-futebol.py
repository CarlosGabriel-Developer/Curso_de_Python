##Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.

tabela_brasileirao_2026 = (
    'Palmeiras', 'Flamengo', 'Atlético-MG', 'Fluminense', 'Grêmio',
    'Botafogo', 'São Paulo', 'Athletico-PR', 'Internacional', 'Fortaleza',
    'Corinthians', 'Cruzeiro', 'Bahia', 'Vasco', 'Santos',
    'Red Bull Bragantino', 'Cuiabá', 'Goiás', 'Coritiba', 'América-MG'
)
print(f"Os 5 primeiros times são :{tabela_brasileirao_2026[:5]} ")
print(f"Os últimos 4 colocados são : {tabela_brasileirao_2026[-4:]}")
print(f'Times em ordem alfabética : {sorted(tabela_brasileirao_2026)}')


if "Bahia" in tabela_brasileirao_2026 : 
    posicao = tabela_brasileirao_2026.index("Bahia")+1
    
    print(f"A posição do time é a {posicao}")
    
else : 
    
    print("O time não estar na tabela")
    