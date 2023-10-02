# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista

lista = []
var = 4

while var <= 20:
    if var % 2 == 0:
        lista.append(var)
        var+=1
    else:
        var+=1

print(lista)
