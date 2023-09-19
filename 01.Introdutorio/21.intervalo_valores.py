for i in range(1,11):
    print (i)

#range(valor_inicial,valor_final,salto_valor) range de 1 a 10: range(1,11), range de 1 a 20, saltando 2: range(1,21,2)
for i in range(50,101,2):
    print(i)

for i in range(0,-20,-2):
    print(i)

# Usando o tamanho de uma lista na função range()
lista = ["Abacaxi","Banana","Morango","Uva"]
lista_tamanho = len(lista)
for i in range(0,lista_tamanho):
    print(lista[i])