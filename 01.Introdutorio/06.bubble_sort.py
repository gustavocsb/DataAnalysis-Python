def bubble_sort(arr):

    # definindo o tamanho do array
    tamanho = len(arr)

    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

lista = [6,7,8,3,10,19,4,1,0,61,30,16,17,82,29,34,43,21,11,39,56,67,12]

#print(lista.sort())
print(bubble_sort(lista))

