def cortar_cuerda(largo, precio, longitud_total): # Funcion para calcular el precio máximo al cortar la cuerda
    n = len(largo)
    matriz = [0] * (longitud_total + 1)

    for i in range(1, longitud_total + 1): # Itera a través de todas las longitudes posibles
        max_precio = float('-inf')
        for j in range(1, min(i, n) + 1): # Itera a través de los cortes posibles
            max_precio = max(max_precio, precio[j - 1] + matriz[i - j]) # Calcula el precio máximo considerando todos los cortes posibles
        matriz[i] = max_precio

    return matriz[longitud_total] # Retorna la matriz de la longitud total


def descomposicion_optima(largo, precio, longitud_total): # Funcion para obtener la descomposicion optima de la cuerda
    n = len(largo)
    matriz = [0] * (longitud_total + 1)
    cortes = [0] * (longitud_total + 1)

    for i in range(1, longitud_total + 1): # Itera a través de todas las longitudes posibles
        max_precio = float('-inf')
        mejor_corte = 0
        for j in range(1, min(i, n) + 1): # Itera a través de los cortes posibles
            if precio[j - 1] + matriz[i - j] > max_precio: # Encuenrtra el corte que maximiza el precio
                max_precio = precio[j - 1] + matriz[i - j]
                mejor_corte = j
        matriz[i] = max_precio
        cortes[i] = mejor_corte

    descomposicion = []
    i = longitud_total
    while i > 0: # Reconstruye la descomposición óptima
        corte_actual = cortes[i]
        descomposicion.append(corte_actual)
        i -= corte_actual

    return descomposicion # Retorna la descomposicion de la cuerda

#largo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#precio = [1, 5, 0, 9, 10, 17, 17, 20, 24, 30]
#longitud_total = 10

largo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # Largo de la cuerda
precio = [1, 4, 10, 12, 15, 20, 21, 32, 31, 41, 51] # Precio de la cuerda
longitud_total = 11 # Longitud maxima

precio_maximo = cortar_cuerda(largo, precio, longitud_total) # Calcula precio máximo y descomposición óptima
descomposicion = descomposicion_optima(largo, precio, longitud_total)

# Mostrar resultados
print("El precio máximo para la cuerda de longitud {} es: {}".format(longitud_total, precio_maximo)) # Imprime el resultado de la cuerda
print("La descomposicion optima es: {}".format(descomposicion)) # Imprime el resultado de la descomposicion



#largo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#precio = [1, 5, 0, 9, 10, 17, 17, 20, 24, 30]
#longitud_total = 10