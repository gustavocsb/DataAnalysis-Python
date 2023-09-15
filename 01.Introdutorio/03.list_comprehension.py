nums = list(range(1,101))

# sintaxe mais curta para criar uma lista baseado em valores de uma lista já existente.
lista_divisao = [num for num in nums if num % 2 == 0 and num % 4 == 0]

print(lista_divisao)