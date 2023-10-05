#Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

#PASSO 1 - Crie, Armazene, e peça ao usuário as suas notas!
nota1 = int(input(f"Digite sua Notas: "))
nota2 = int(input(f"Digite sua segunda nota"))

print("Nota 1 Identificada :", nota1,", Nota 2 Identificada: ", nota2)
#PASSO 2 - Calcule a média das duas notas!
media = (nota1 + nota2) / 2

#PASSO 3 - Use if para testar se o aluno/usuário foi Aprovado
#reprovado e se for 10 aprovado com distição e imprima.
print("Sua média é: ",media)
if media == 10:
    print(f"Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
