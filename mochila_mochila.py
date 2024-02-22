def mochila(valor, peso, capacidad): # Funcion para calcular el valor optimo y peso de la mochila
    n = len(valor)
    matriz = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]  # Inicia la matriz de soluciones parciales

    for i in range(1, n + 1): # Llena la matriz utilizando la relación de recurrencia
        for j in range(capacidad + 1):
            if peso[i - 1] <= j: # Toma el máximo entre el valor actual y el valor sin incluir el objeto
                matriz[i][j] = max(valor[i - 1] + matriz[i - 1][j - peso[i - 1]], matriz[i - 1][j])
            else:
                matriz[i][j] = matriz[i - 1][j] # Si el peso del objeto es mayor que la capacidad actual, no se incluye

    valor_optimo = matriz[n][capacidad] # Reconstruye la solución
    objetos_seleccionados = [] # Genera un nuevo array con los objetos

    i, j = n, capacidad
    while i > 0 and j > 0: # Empieza a generar el array con los objetos que cumplan con el peso
        if matriz[i][j] != matriz[i - 1][j]:
            objetos_seleccionados.append(i)
            j -= peso[i - 1]
        i -= 1

    return valor_optimo, objetos_seleccionados[::-1] # Retorna el valor optimo y objetos ideales, de manera ascendente


valor = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59] # Valor
peso = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52] # Peso
capacidad_maxima = 140 # Variable para determinar el peso maximo


valor_optimo, objetos_seleccionados = mochila(valor, peso, capacidad_maxima) # Pasamos la funcion para resolver el problema
print("El valor óptimo de la mochila es: {}".format(valor_optimo)) # Imprime el resultado del valor optimo
print("Los objetos seleccionados son: {}".format(objetos_seleccionados)) # Imprime los mejores objetos para la mochila


