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

arr6 = np.diag(np.array([1,2,3,4])) # A função diag() cria um array NumPy com os elementos da diagonal principal - diag(array)
print(f'Array 6 (com diag): \n{arr6}\n')

arr7 = np.array([True, False, False, True])
print(f'Array 7 (com valores booleanos): {arr7}\n')

arr8 = np.array(['Python', 'NumPy', 'Pandas', 'Matplotlib'])
print(f'Array 8 (com strings): {arr8}\n')

# A função linspace() cria um array NumPy contendo uma progressão aritmética a partir de um intervalo - linspace(start, stop, num)
# retorna um array com num elementos igualmente espaçados entre start e stop
arrlinspace = np.linspace(0,10)
print(f'Array com linspace(0,10): \n{arrlinspace}\n')
arrlinspace2 = np.linspace(0,10,15)
print(f'Array com linspace(0,10,15): \n{arrlinspace2}\n')

# A função logspace() cria um array NumPy contendo uma progressão aritmética a partir de um intervalo - logspace(start, stop, num)
arrlogspace = np.logspace(0,10)
print(f'Array com logspace(0,10): \n{arrlogspace}\n')
arrlogspace2 = np.logspace(0,10,15)
print(f'Array com logspace(0,10,15): \n{arrlogspace2}\n')



print('---------------------------------------------------- Manipulando Matrizes ----------------------------------------------------\n')
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f'Matriz: \n{matriz}')
print(f'Type: {type(matriz)}')
print(f'Shape: {matriz.shape}\n')

# Criando uma matriz 2x3 apenas com números 1
matrizones = np.ones((2,3))
print(f'Matriz com ones(2,3): \n{matrizones}\n')

# Lista de listas
lista = [[13,81,22],[0,34,59],[21,48,94]]
print(f'Lista de listas: {lista}\n')

# Função matrix() cria uma matriz a partir de uma lista de listas
matrix = np.matrix(lista)
print(f'Matriz a partir da lista de listas: \n{matrix}')
print(f'Type: {type(matrix)}')
print(f'Shape: {matrix.shape}')
print(f'Size: {matrix.size}\n')

# Indexação da matriz
print(f'Elemento na linha 2, coluna 1 da matriz: {matrix[2,1]}')

# Todos elementos que estejam nas linhas entre 0 e 2 índice 2 na coluna
print(f'Elementos na coluna 2 das linhas 0 a 2 da matriz: \n{matrix[0:2,2]}')

# Indexação da matriz matrix[1,]
print(f'Elementos da linha 1 da matriz: \n{matrix[1,]}\n')

# Alterando um elemento da matriz
print(f'Matriz antes da alteração: \n{matrix}')
matrix[1,0] = 100
print(f'Matriz com o elemento da linha 1, coluna 0 alterado: \n{matrix}\n')

x = np.array([1,2]) # NumPy decide o tipo dos dados
y = np.array([1.0,2.0]) # NumPy decide o tipo dos dados
z = np.array([1,2], dtype=np.float64) # Forçando o tipo dos dados
print(f'Array x: {x}')
print(f'Array y: {y}')
print(f'Array z: {z}\n')

print(f'Tipo de x: {x.dtype}')
print(f'Tipo de y: {y.dtype}')
print(f'Tipo de z: {z.dtype}\n')

# Criar um array com lista de listas com dtype = float
dtype_matriz = np.array([[24,76,92,14],[47,35,89,2]], dtype=float)
print(f'Matriz com dtype float: \n{dtype_matriz}\n')

# O itemsizes retorna o tamanho em bytes de cada elemento do array. Em outras palavras, o itemsize representa o número de bytes que cada elemento do array ocupa na memória
print(f'Tamanho em bytes de cada elemento do array: {dtype_matriz.itemsize}')

# O nbytes retorna o tamanho em bytes do array. Em outras palavras, o nbytes representa o número total de bytes que o array ocupa na memória
print(f'Tamanho total em bytes do array: {dtype_matriz.nbytes}')

# O ndim retorna o número de dimensões do array
print(f'Número de dimensões do array: {dtype_matriz.ndim}\n')


# Criando um array numpy de 3 dimensões
arr_3d = np.array([
    [
        [1,2,3,4]
        ,[5,6,7,8]
        ,[9,10,11,12]
    ],
    [
        [13,14,15,16]
        ,[17,18,19,20]
        ,[21,22,23,24]
    ]
])

print(f'Array 3D: \n{arr_3d}') # Cada cochete no numpy representa uma dimensão no print
print(f'Número de dimensões do array 3D: {arr_3d.ndim}')
print(f'Shape do array 3D: {arr_3d.shape}\n')

# Criando um array numpy de 4 dimensões

arr_4d = np.array([
    [
        [
            [1,2,3,4,5]
            ,[6,7,8,9,10]
            ,[11,12,13,14,15]
            ,[16,17,18,19,20]
        ],
        [
            [21,22,23,24,25]
            ,[26,27,28,29,30]
            ,[31,32,33,34,35]
            ,[36,37,38,39,40]
        ],
        [
            [41,42,43,44,45]
            ,[46,47,48,49,50]
            ,[51,52,53,54,55]
            ,[56,57,58,59,60]
        ],
        [
            [61,62,63,64,65]
            ,[66,67,68,69,70]
            ,[71,72,73,74,75]
            ,[76,77,78,79,80]
        ],
        [
            [81,82,83,84,85]
            ,[86,87,88,89,90]
            ,[91,92,93,94,95]
            ,[96,97,98,99,100]
        ]
    ]
])

print(f'Array 4D: \n{arr_4d}') # Cada cochete no numpy representa uma dimensão no print
print(f'Número de dimensões do array 4D: {arr_4d.ndim}')
print(f'Shape do array 4D: {arr_4d.shape}\n')