import numpy as np

arr1 = np.diag(np.arange(3))
print(f'Matriz Diagonal: \n{arr1}\n')

print(f'Elemento 1,1: {arr1[1,1]}\n')
print(f'Coluna 1: {arr1[1]}\n')
print(f'Coluna 2: {arr1[:,2]}\n')

arr2 = np.arange(10)
print(f'Array: {arr2}')

# [start:end:stop]
arr2[2:9:3]

a = np.array([1,2,3,4])
b = np.array([4,2,2,4])

print(a == b)

print(f'Comparação de Arrays [arr1] e [arr2]: {np.array_equal(arr1, arr2)}\n')

print(f'Min: {arr1.min()}')

print(f'Max: {arr1.max()}')

# Somando um valor a cada elemento do array
print(f'Array + 1.5: {np.array([1,2,3]) + 1.5}\n')

# Cria um array com números decimais
arr3 = np.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])

print(f'Array: {arr3}')

# Arredonda os valores do array
print(f'Arredondamento: {np.round(arr3)}\n')

arr4 = np.array([[1,2,3,4], [5,6,7,8]])
print(f'Matriz: \n{arr4}')

# O método flatten() com NumPy é usado para criar uma cópia unidimensional ("achatada" flatten) de um array multidimensional. Isso significa que o método cria um novo
# array unidimensional, que contém todos os elementos do array multidimensional original, mas que está organizado em uma única linha. A ordem dos elementos no novo array
# unidimensional segue a ordem dos elementos no array multidimensional original.

# "Achatando" a matriz (flatten)
print(f'Matriz "achatada": {arr4.flatten()}\n')

arr5 = np.array([1,2,3])
print(f'Array: {arr5}')

# Repetindo os elementos de um array com repeat
print(f'Array repetido 3 vezes com repeat(): {np.repeat(arr5, 3)}')

# Repetindo os elementos de um array com tile
print(f'Array repetido 3 vezes com tile(): {np.tile(arr5, 3)}\n')

arr6 = np.array([5, 6])

# Criando a cópia de um array
arr7 = arr6.copy()

print(f'Array 6: {arr6}\nArray 7 (cópia de Array 6): {arr7}\n')