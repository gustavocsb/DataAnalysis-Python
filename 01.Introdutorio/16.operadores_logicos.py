idade = 18
nome = "Bob"
if idade > 17:
    print("Você pode tirar sua CNH!")

idade = 18
if idade > 17 and nome == "Bob":
    print("Autorizado!")

# Operadores lógicos:
# and - retorna True se ambas declarações forem verdadeiras
# or - retorna True se uma das declarações for verdadeira.
# not - inverte o resultado, retorna False se o resultado normalmente for True

numero = 4
if (numero > 2) and (numero % 2 == 0):
    print("Isso está sendo impresso porque as duas condições são verdadeiras!")

numero = 4
if (numero > 5) and (numero % 2 == 0):
    print("Isso está sendo impresso porque as duas condições são verdadeiras!")
else:
    print("Isso está sendo impresso porque uma das duas condições é falsa!")

numero = 4
if (numero > 5) or (numero % 2 == 0):
    print("Isso está sendo impresso porque uma das condições é verdadeira!")

numero = 4
if not(numero > 5) and (numero % 2 == 0):
    print("Isso está sendo impresso porque as duas condições são verdadeiras!")
else:
    print("Isso está sendo impresso porque uma das duas condições é falsa!")

disciplina = "Data Science"
nota_final = 70
if disciplina == "Data Science" and nota_final >= 70:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado!")

disciplina = "Data Science"
nota_final = 60
if disciplina == "Data Science" and nota_final >= 70:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado!")

disciplina = "Data Science"
nota_final = 90
semestre = 2
if disciplina == "Data Science" and nota_final >= 80 and semestre != 1:
    print(f"Você foi aprovado em {disciplina} com média final {nota_final}!")
else:
    print("Lamento, acho que você precisa estudar mais!")
