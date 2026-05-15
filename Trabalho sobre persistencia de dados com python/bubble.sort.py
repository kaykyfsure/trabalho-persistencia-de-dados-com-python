def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                variavel_auxiliar = array[j]
                array[j] = array[j + 1]
                array[j + 1] = variavel_auxiliar

meu_array = [54, 26, 93, 17, 77, 31, 44, 55, 20, 14, 82, 63, 12, 99, 5]

print("Array original: ", meu_array)


bubbleSort(meu_array)


print("Array ordenado: ", meu_array)