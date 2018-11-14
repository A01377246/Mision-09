# Autor: Humberto Carrillo
# Descripción: Programa con varias funciones que están relacionadas con listas.


def extraerPares(listaEnteros):  # Recibe una lista de enteros, la visita y crea una nueva lista que contiene los pares.
    listaPares = []
    for dato in listaEnteros:    # Visitar cada dato de la lista
        if dato % 2 == 0:        # Operador Módulo: si el residuo es 0 al dividir entre 2 entonces, es par.
            listaPares.append(dato)  # Agregar los pares a la nueva lista.
        # En caso de que la lista no cuente con ningún valor par, una lista vacía es devuelta.
    return listaPares


def extraerMayoresPrevio(listaNumeros):   # Recibe una lista de numeros y crea una nueva lista con valores mayores.
    listaMayores = []                # Generar una nueva lista donde se guardaran los mayores
    if listaNumeros == []:           # En caso de recibir una lista vacía
        return listaNumeros
    else:
        elementoPrevio = listaNumeros[0] #El elemento previo al inicio es el primer valor
        for dato in listaNumeros:        # Visitar cada dato en la lista
            if dato > elementoPrevio:    # si el dato es mayor que el elemento previo
               listaMayores.append(dato) # Agregar a la lista Mayores ese dato
               elementoPrevio = dato     # Elemento previo ahora será igual al dato agregado
            else:                        # En caso de que el dato no sea mayor que el elemento previo.
               elementoPrevio = dato
        return listaMayores


def intercambiarParejas(listaValores):           # Intercambia las parejas de una lista
    parejasInvertidas= []                        # Lista en la que se guardarán las parejas intercambiadas
    for k in range(len(listaValores)):           # Visitar la lista utilizando índices de posición
        if k % 2 == 0:           # Si el índice es divisible entre 2, entonces está en la primera posición de la pareja
            parejasInvertidas.append(listaValores[k]) # Agregar a la lista todos los valores que cumplan con lo anterior
        else:
            parejasInvertidas.insert(k-1, listaValores[k]) # Agregar en el índice k-1 todos los demás valores.

    return parejasInvertidas


def intercambiarMM(listaNumeros):       # Recibe una lista e intercambia el valor mayor con el menor
    if listaNumeros == []:              # En caso de que la lista este vacía
        return listaNumeros             # Regresar la misma lista
    minimo = min(listaNumeros)          # Encontrar valor mínimo
    maximo = max(listaNumeros)          # Encontrar valor máximo
    posicionMax = listaNumeros.index(maximo)  # Calcular la posición del valor max
    posicionMin = listaNumeros.index(minimo)  # Calcular la posición del valor min
    listaNumeros.remove(listaNumeros[posicionMax])  # Remover el valor máximo
    listaNumeros.remove(listaNumeros[posicionMin])  # Remover el valor mínimo
    listaNumeros.insert(posicionMin, maximo)        # Insertar el valor maximo en la posición del mínimo ahora vacía.
    listaNumeros.insert(posicionMax, minimo)        # Insertar el valor minimo en la posición del máximo ahora vacía.
    return listaNumeros


def promediarCentro(listaPromedio):         # Calcula el promedio centro al recibir una lista con valores
    minimo = min(listaPromedio)             # Calcular el mínimo de la lista
    maximo = max(listaPromedio)             # Calcular el máximo de la lista
    listaPromedio.remove(minimo)            # Quitar el valor mínimo
    listaPromedio.remove(maximo)            # Quitar el valor máximo
    if listaPromedio == []:
        return 0
    promedioCentro = sum(listaPromedio)/len(listaPromedio)  # Calcular el promedio
    return promedioCentro                   # Devuelve el promedio centro


def calcularEstadistica(listaEstadistica):
    suma = sum(listaEstadistica)         # Se suman los valores de la lista para después utilizarse en la media.
    largoLista = len(listaEstadistica)   # Calcular el número de datos,
    if largoLista == 0:                  # En caso de que se presente una lista vacía
        media = 0
        return 0, 0                      # Si hay una lista vacia devuelve 0,0
    else:
        media = suma / largoLista          # Calculo de la media
        contadorSumatoria = 0              # Establecer un contador para la sumatoria
        for valor in listaEstadistica:     # Visitar cada dato con el fin de obtener su desviación
            distanciaDato = (valor - media)**2  # Calcular la distancia de cada dato con respecto a la media
            contadorSumatoria = contadorSumatoria + distanciaDato # Sumar las distancias de todos los datos

        desviacion = (contadorSumatoria / (largoLista-1)) ** (1 / 2)  # Calcular la desviación según la fórmula.
        return media, desviacion  # Devolver dupla media, desviación.

def main():

    # Pruebas problema 1:
    listaEnterosA = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]   # Regresa una nueva lista: [2,2,4,60,8,22,4]
    listaEnterosB = [5, 7, 3]  # Regresa una nueva lista: []
    listaEnterosC = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 104, 226]  # Regresa una nueva lista con los mismos valores
    listaEnterosD = []  # Regresa una nueva lista: []
    print(extraerPares(listaEnterosA))
    print(extraerPares(listaEnterosB))
    print(extraerPares(listaEnterosC))
    print(extraerPares(listaEnterosD))

    # Pruebas problema 2:
    listaNumerosA = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaNumerosB = [5,4,3,2]
    listaNumerosC = []
    print(extraerMayoresPrevio(listaNumerosA))
    print(extraerMayoresPrevio(listaNumerosB))
    print(extraerMayoresPrevio(listaNumerosC))
    # Pruebas problema 3:
    listaValoresA = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]  # Regresa una nueva lista: [2,1,2,3,60,4,8,5,22,3,55,44)
    listaValoresB = [7]       # Regresa una nueva lista: [7]
    listaValoresC = []        # Regresa una nueva lista: []
    listaValoresD = [1, 2]     # Regresa una nueva lista :[2,1]
    print(intercambiarParejas(listaValoresA))
    print(intercambiarParejas(listaValoresB))
    print(intercambiarParejas(listaValoresC))
    print(intercambiarParejas(listaValoresD))

    # Pruebas problema 4:
    listaNumerosA = [5, 9, 3, 22, 19, 31, 10, 7]
    listaNumerosB = [1, 2, 3]
    listaNumerosC = []
    print(intercambiarMM(listaNumerosA))
    print(intercambiarMM(listaNumerosB))
    print(intercambiarMM(listaNumerosC))
    


    # Pruebas problema 5:
    listaPromedioA = [70, 80, 90]  # Regresa el promedio central: 80
    listaPromedioB = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]  # Regresa el promedio central:63. 62.5 es redondeado
    listaPromedioC = [20, 55, 30, 5, 55, 5]  # Regresa el promedio central: 28.
    listaPromedioD = [5, 9, 1, 8]  # Regresa el promedio central: 6
    listaPromedioE = [5, 8]   # Regresa el promedio central: 0
    print("%.f" % (promediarCentro(listaPromedioA)))
    print("%.f" % (promediarCentro(listaPromedioB)))  # Se da formato para evitar que aparezca un 62.5
    print("%.f" % (promediarCentro(listaPromedioC)))  # Desgraciadamente, el formato redondea hacia arriba y obtenemos
    print("%.f" % (promediarCentro(listaPromedioD)))  # un 63 en lugar de 62
    print("%.f" % (promediarCentro(listaPromedioE)))

    # Pruebas problema 6:
    listaEstadisticaA = [1, 2, 3, 4, 5, 6]          # Regresa (3.5, 1.8708)
    listaEstadisticaB = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]   # Regresa (62.0, 30.2324)
    listaEstadisticaC = []                          # Regresa (0,0)
    print(calcularEstadistica(listaEstadisticaA))
    print(calcularEstadistica(listaEstadisticaB))
    print(calcularEstadistica(listaEstadisticaC))

main()

