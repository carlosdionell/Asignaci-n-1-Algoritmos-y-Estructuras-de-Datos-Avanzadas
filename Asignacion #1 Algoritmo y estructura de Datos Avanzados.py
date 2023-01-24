
print("Algoritmos y Estructuras de Datos Avanzadas")

print("Carlos Rivera")

print("Asignación")

print("Desarrollar algoritmo de Ordenamiento") 

"""Desarrollar un programa (en el lenguaje de programación de su preferencia) que realice el algoritmo de Ordenamiento por 
Selección de un arreglo numérico de 9 elementos. Tome como referencia el siguiente arreglo para su prueba unitaria:
90, 15, 82, 16, 20, 17, 6, 1, 43."""
"""
[90, 15, 82, 16, 20, 17, 6, 1, 43]
tamaño : 9
indice a cambiar: 0
elemento del indice a cambiar: 90
hacer comparaciones para intercambiar los valores
nuevo indice : 1
nuevo elemento de ese indic: 15
[90, 15, 82, 16, 20, 17, 6, 1, 43] hasta llegar al ultimo indice
"""
array = [90, 15, 82, 16, 20, 17, 6, 1, 43] # array con elemntos númericos
print(f'Array inicial {array}')
# tomar un elemento a la vez y compararlo para intercambiarlo con un nuevo menor
for i in range(0,len(array)):
    minValue = array[i] # elemento seleccionado a itercambiar para compararlo si es que no existe un valor mas pequeño 
    minIndex = i # la posicion donde esta ubicado el elemento a intercambiar
    #for j,el in enumerate(array)
    for j in range(minIndex+1,len(array)):
        if array[j] < minValue:
            minValue = array[j]
            minIndex = j
    temp = array[i] # 10
    array[i] = minValue 
    array[minIndex] = temp 

print(f'Array final {array}')

