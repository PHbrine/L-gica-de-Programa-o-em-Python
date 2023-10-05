#Pergunte ao usuário sobre o preço de um item que deseja comprar
# e o valor disponível em sua carteira.
# Use uma estrutura condicional para decidir se ele pode comprar o item ou não
#Informe a decisão ao usuário.~

#passo 1 - Crie e armazene a variavel carteira e peça o usuário para digitar
carteira = float(input("Informe a quantia que sua carteira possui"))

#PASSO 2 - crie e armazene a variável produto e Peça ao usuário o valor do produto
produto = float(input(f"Qual o valor do produto"))

#passo 3 - informe ao usuário se o valor do produro condiz com o que tem na certeira
if carteira <= produto: print("Valor insuficiente")
else:
    print("é possível comprar")

    #Atividade feita em 29.09 20:20