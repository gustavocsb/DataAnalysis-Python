# A função reduce() em Python é uma função da biblioteca functools que aplica uma determinada função binária a pares consecutivos de elementos em uma
# estrutura de dados iterável(como uma lista, tupla ou outro objeto iterável), reduzindo-a um único valor

# Importando a função reduce do módulo functools
from functools import reduce

from  IPython.display import Image

Image(r"01.Introdutorio\reduce.png")

lista = [47,11,42,13]
print(lista)

def soma(a,b):
    x=a+b
    return x

# Usando reduce com uma função e uma lista. A função vai retornar o valor máximo
print(reduce(soma,lista))

lst = [47,11,42,13]

# Usando a função reduce() com lambda

print(reduce(lambda x,y: x+y, lst))

# Podemos atribuir a expressão lambda a uma variável
find_max = lambda a,b: a if (a>b) else b

print(type(find_max))

print(reduce(find_max, lst))