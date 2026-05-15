array = [85, 24, 63, 45, 17, 31, 96, 50, 4, 78, 22, 69, 12, 90, 33]
print("Array original: ", array)

for i in range(len(array)):
    
    indice_menor = i
    for j in range(i + 1, len(array)):
        if array[indice_menor] > array[j]:
            
            indice_menor = j
            
    auxiliar = array[i]
    array[i] = array[indice_menor]
    array[indice_menor] = auxiliar
print("Array ordenado: ", array)