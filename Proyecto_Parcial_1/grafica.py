"""
Módulo encargado de generar
la gráfica de regresión lineal.
"""

import matplotlib.pyplot as plt


def mostrar_grafica(x, y, m, b):
    """
    Muestra:

    - Los puntos originales.
    - La recta de regresión.
    - La ecuación de la recta.
    """

    # Obtener los valores mínimo y máximo de x
    x_min = min(x)
    x_max = max(x)

    # Crear dos puntos para dibujar la recta
    x_recta = [
        x_min,
        x_max
    ]

    # Calcular los valores y correspondientes
    y_recta = [
        m * valor + b
        for valor in x_recta
    ]

    # Crear la figura
    plt.figure(figsize=(9, 6))

    # Dibujar los datos originales
    plt.scatter(
        x,
        y,
        label="Muestras"
    )

    # Dibujar la recta de ajuste
    plt.plot(
        x_recta,
        y_recta,
        label="Recta de ajuste"
    )

    # Título
    plt.title(
        "Regresión Lineal por Mínimos Cuadrados"
    )

    # Nombre de los ejes
    plt.xlabel("X")
    plt.ylabel("Y")

    # Mostrar cuadrícula
    plt.grid(True, alpha=0.3)

    # Mostrar leyenda
    plt.legend()

    # Crear la ecuación
    ecuacion = (
        f"y = {m:.4f}x + {b:.4f}"
    )

    # Mostrar la ecuación dentro de la gráfica
    plt.text(
        0.05,
        0.95,
        ecuacion,
        transform=plt.gca().transAxes,
        verticalalignment="top"
    )

    # Ajustar distribución
    plt.tight_layout()

    # Mostrar gráfica
    plt.show()