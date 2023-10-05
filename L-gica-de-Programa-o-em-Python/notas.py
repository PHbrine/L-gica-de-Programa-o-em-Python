#Peça ao usuário que insira sua nota em um exame.t
# Use estruturas condicionais para determinar e informar se a
# nota é A, B, C, D ou F com base em uma escala predefinida de notas.

# Passo 1 - Crie e armazene a variavel nota do usuário
print("Digite sua nota em número: ")
nota = float(input())

# Passo 2 - categorize e exiba a nota em escala
if nota >= 9: print("Sua nota é A")

elif nota >= 7 and nota <= 8.9: print("Sua nota é B")

elif nota >= 5 and nota <= 6.9: print("Sua nota é C")

elif nota >= 3 and nota <= 4.9: print ("Sua nota é D")

elif nota >= 2 and nota <= 2.9: print ("Sua nota é E")

elif nota <= 1.9: print("Sua nota é F")
