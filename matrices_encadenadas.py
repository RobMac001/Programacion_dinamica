def parentizacion_optima(p): # Funcion para calcular la parentizacion optima de los valores
    n = len(p) - 1
    m = [[float('inf')] * n for _ in range(n)] # Creamos una matriz para almacenar los resultados de los subproblemas
    s = [[0] * n for _ in range(n)]

    for i in range(n): # Inicia la diagonal de la matriz con ceros
        m[i][i] = 0

    for l in range(2, n + 1): # Se llena la matriz utilizando programación dinámica
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k + 1

    def construir_parentizacion(i, j): # Se construye la parentización óptima
        if i == j:
            return f"A{i + 1}"
        else:
            return f"({construir_parentizacion(i, s[i][j] - 1)} * {construir_parentizacion(s[i][j], j)})"

    return m[0][n - 1], construir_parentizacion(0, n - 1) # Retornamos el resultado

p = [5, 10, 3, 12, 5, 50, 6] # Datos principales
#p = [30, 35, 15, 5, 10, 20, 25]

min_multiplicaciones, parentizacion_optima = parentizacion_optima(p) # Obtiene la solución  de la parentizacion optima

print("El minimo de multiplicaciones escalares es: {}".format(min_multiplicaciones)) # Imprime el minimo de multiplicaciones
print("La parentizacion optima es: {}".format(parentizacion_optima)) # Imprime la parentizacion optima

