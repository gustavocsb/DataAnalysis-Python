# list: estrutura de dados mutável, sequência ordenada de elementos e variável
# range: sequência de números OBS: Começa no 0 por padrão e incrementa 1 por padrão
nums = list(range(1,101))

# type: mostra qual o tipo de dado da variável
print(type(nums))

# printando apenas os números pares que são divididos por 4
for num in nums:
    if num % 2 == 0 and num % 4 == 0:
        print(num)