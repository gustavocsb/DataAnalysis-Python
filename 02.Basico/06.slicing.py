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