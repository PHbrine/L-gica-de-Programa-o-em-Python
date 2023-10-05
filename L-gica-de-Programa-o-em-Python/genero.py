#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

#Crie, armazene e peça a variável "genero" ao usuário o genero a seguir, F para feminino
#M para Masculino e para qualquer outro, genêro invalido.
print("Informe o seu Gênero:")
genero = str(input())

#passo 2 - teste para saber qual o genero recebe e imprima o resultado.
if genero == "f" :
    print("Feminino")
elif genero == "m":
    print("Masculino")
else:
    print("Gênero invalido")