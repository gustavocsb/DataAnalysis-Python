import numpy as np

arr1 = np.arange(1,10)
print(f'Array: {arr1}')
print(f'Soma: {np.sum(arr1)}')
print(f'Produto: {np.prod(arr1)}')
print(f'Soma Acumulada: {np.cumsum(arr1)}\n')

arr2 = np.array([3,2,1])
arr3 = np.array([1,2,3])
print(f'Array A: {arr2}')
print(f'Array B: {arr3}')

arrSum = np.add(arr2, arr3)
print(f'Array A + Array B: {arrSum}\n')

arr4 = np.array([[1,2],[3,4]])
arr5 = np.array([[5,6],[0,7]])
print(f'Shape Matriz A: {arr4.shape}')
print(f'Matriz A: \n{arr4}\n')
print(f'Shape Matriz B: {arr5.shape}')
print(f'Matriz B: \n{arr5}\n')

# Multiplicando as duas matrizes
arrMult = np.dot(arr4, arr5)
print(f'Multiplicação Matriz A * Matriz B: \n{arrMult}\n') # Para usar o método dot, o número de colunas da matriz A deve ser igual ao número de linhas da matriz B

# O que aconteceu ao executar a multiplicação das matrizes:
for i in range(arrMult.shape[0]):
    for j in range(arrMult.shape[1]):
        print(f'O elemento {i+1},{j+1} foi obtido com [{arr4[i,0]}*{arr5[0,j]} + {arr4[i,1]}*{arr5[1,j]}] = {arrMult[i,j]}')