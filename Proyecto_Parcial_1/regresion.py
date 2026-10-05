"""
Módulo para calcular la regresión lineal
por mínimos cuadrados.
"""


def calcular_regresion(x, y):
    """
    Calcula la pendiente m y el intercepto b
    de la recta:

        y = mx + b

    Parámetros:
        x: lista de valores independientes.
        y: lista de valores dependientes.

    Regresa:
        m: pendiente.
        b: intercepto.
    """

    # Comprobar que las listas tengan
    # la misma cantidad de elementos.
    if len(x) != len(y):
        raise ValueError(
            "Las listas x e y deben tener "
            "la misma cantidad de elementos."
        )

    # Número de muestras
    n = len(x)

    if n < 2:
        raise ValueError(
            "Se necesitan al menos dos muestras."
        )

    # Sumas necesarias para las fórmulas
    suma_x = sum(x)

    suma_y = sum(y)

    suma_xy = sum(
        xi * yi
        for xi, yi in zip(x, y)
    )

    suma_x2 = sum(
        xi ** 2
        for xi in x
    )

    # Denominador de la fórmula de m
    denominador = (
        n * suma_x2
        - suma_x ** 2
    )

    # Evitar división entre cero
    if denominador == 0:
        raise ValueError(
            "No se puede calcular la pendiente "
            "porque todos los valores de x son iguales."
        )

    # Calcular pendiente
    m = (
        n * suma_xy
        - suma_x * suma_y
    ) / denominador

    # Calcular intercepto
    b = (
        suma_y
        - m * suma_x
    ) / n

    return m, b