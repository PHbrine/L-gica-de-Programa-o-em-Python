#passo 1  - Crie, armazene e peça ao usuário para digitar o peso!
print("Digite seu PESO: ")
peso = float(input())
print("==")
#passo 2 - Crie, armazene e peça ao usuário para digitar a altura!
print("Digite sua ALTURA: ")
altura = float(input())
print("==")
#passo 3 - calcule imc e crie a variavel categoria
imc = int =  peso / (altura * altura)

categoria = imc
#passo 4 - informe o padrão do imc
print(imc,"KG")
print("==")

if categoria <= 18.5: print("Vocẽ está abaixo do peso")
elif categoria >= 18.5 and categoria <= 24.9: print("Interválo saudável")
elif categoria >= 25.0 and categoria <= 29.9: print("Está levemente acima do peso")
elif categoria >= 30 and categoria  <= 34.9: print("Está com obesididade leve")
elif categoria >= 35 and categoria <= 39.9: print("Está com Obesidade moderada")
elif categoria >= 40: print("Está em obesidade gravissimo")

#atividade feita em 29.09 21:03
