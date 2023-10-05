# Passo 1 - Criar e armazenar a variavel peso e altura
# Passo 2 - pedir ao usuário cada variável
print("Informe seu peso")
peso = float(input())

print("Infome sua altura")
altura = float(input())

# Passo 3 - Calcular o peso e a altura coma  formula imc
imc = int (peso / (altura * altura))

# Passo 4 - Testar o valor IMC e categorizá-l0
# Passo 5 - Informar imc e a categoria

print("Seu IMC é: ", imc, "KG")

if imc <= 16:
    print("Seu Peso é frango NV III")
elif imc <= 16.9:
    print("Seu Peso é Frango NV II")
elif imc <= 18.4:
    print("Seu Peso é Frango NV I")
elif imc <= 24.9:
    print("Seu Peso é Adequado")
elif imc <= 34.4:
    print("Seu Peso é ACIMA DO NORMAL")

#ATIVIDADE FEITA 28.09 - 02:58






