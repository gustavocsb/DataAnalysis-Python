lista1 = [0,1,2,3,4]
lista2 = [1,2,3]

for elemento_lista1 in lista1:
    for elemento_lista2 in lista2:
        print("\n", elemento_lista1 * elemento_lista2)
    print("----")


# O número 47 aparece nas duas listas?
lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
# Loop externo
for elemento_lista1 in lista1:
    # Loop interno
    for elemento_lista2 in lista2:
        # Condicional
        if elemento_lista1 == 47 and elemento_lista2 == 47:
            print("O número 47 foi encontrado nas duas listas!")


# Some os números pares da primeira lista com os números pares da segunda lista
lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0
# Loop externo
for lista in [lista1, lista2]:
    # Loop interno
    for num in lista:
        # Condicional
        if num % 2 == 0:
            soma+= num
print(f"A soma dos números pares das duas listas é igual a {soma}")


# Listas podem ser concatenadas em Python
lista1 + lista2
# Some os números pares da primeira lista com os números pares da segunda lista
lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0
for num in lista1 + lista2:
    if num % 2 == 0:
        soma += num
print(f"Soma dos valores pares: {soma}")


# Loop em lista de listas (matrizes) para encontrar o maior número
matriz = [[42,23,34], [100,215,114], [10.1,98.7,12.3]]
maior_numero = 0
# Loop externo
for linha in matriz:
    # Loop interno
    for num in linha:
        # Condicional
        if num > maior_numero:
            maior_numero = num
print(f"O maior número da matriz é: {maior_numero}")


# Listando as chaves de um dicionário
dict = {"k1":"Python", "k2":"R", "k3":"Scala"}
for item in dict:
    print(item)
# Imprimindo chave e valor do dicionário. Usando o método items() para retornar os itens de um dicionário
for k, v in dict.items():
    print(k, v)