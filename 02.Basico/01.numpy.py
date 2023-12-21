# ---------------------------------------------------- Numerical Python - https://numpy.org/ ---------------------------------------------------- #

import numpy as np
print(f'Versão do NumPy: {np.__version__}\n')

# Criando arrays com NumPy
arr1 = np.array([11,1231,45,19,25,57,10,32,76])
print(f'Array 1: {arr1}')
print(f'Type: {type(arr1)}')
# 1D Array shape: (x,) ; 2D Array shape: (x,y) ; 3D Array shape: (x,y,z)
# Arrays não se limitam a 3 dimensões, é possível um número infinito de dimensões, porém o cérebro humano não consegue visualizar mais que 3 dimensões
print(f'Shape: {arr1.shape}\n')

# Imprimindo um elemento específico do array
print(f'Elemento no index 4 do array: {arr1[4]}')

# Indexação
print(f'Elementos do index 0 ao 4 do array: {arr1[0:5]}') # O último elemento não é incluído

# Criando uma lista de índices
indices = [1,2,5,6]
# Imprimindo elementos do array com base na lista de índices
print(f'Elementos do array nos índices {indices}: {arr1[indices]}\n')

# Criando uma máscara booleana para os elementos pares
mask = (arr1 % 2 == 0)
print(f'Máscara booleana de números pares: {mask}')
print(f'Elementos pares do array: {arr1[mask]}\n')

# Alterando um elemento do array
print(f'Array antes da alteração: {arr1}')
arr1[0] = 100
print(f'Array com o elemento do index 0 alterado: {arr1}\n')

# Não é possível incluir elementos de tipos diferentes em um array
try:
    arr1[0] = 'Testando elemento novo'
except:
    print('Não é possível incluir elementos de tipos diferentes em um array!\n')


print('---------------------------------------------------- Funções NumPy ----------------------------------------------------\n')

arr2 = np.array([1,2,3,4,5,6,7,8,9,10])

print(f'Array 2: {arr2}\n')
print(f'Type: {type(arr2)}')
print(f'Shape: {arr2.shape}\n')

# Usando métodos do array NumPy

print(f'Soma cumulativa dos elementos do array: {arr2.cumsum()}')
print(f'Produto cumulativo dos elementos do array: {arr2.cumprod()}\n')

arr3 = np.arange(0,50,5)
print(f'Array 3 (com arange): {arr3}') # A função arange() cria um array NumPy contendo uma progressão aritmética a partir de um intervalo - arange(start, stop, step)
print(f'Type: {type(arr3)}')
print(f'Shape: {arr3.shape}\n')

arr4 = np.zeros(10) # A função zeros() cria um array NumPy contendo zeros - zeros(shape)
print(f'Array 4 (com zeros): {arr4}\n')

arr5 = np.eye(3) # A função eye() retorna 1 nas posições diagonais e 0 nas demais - eye(N)
print(f'Array 5 (com eye): \n{arr5}\n')