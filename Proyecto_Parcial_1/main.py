"""
Proyecto Parcial 1 - Ciencia de Datos
Regresión Lineal por Mínimos Cuadrados.

Archivo principal del programa.
"""

from datos import leer_datos
from regresion import calcular_regresion
from grafica import mostrar_grafica


def main():
    """
    Función principal del programa.
    """

    archivo = "datos.csv"

    try:
        # Leer los datos del archivo CSV
        x, y = leer_datos(archivo)

        # Calcular la pendiente y el intercepto
        m, b = calcular_regresion(x, y)

        # Mostrar los resultados en consola
        print("=" * 55)
        print("REGRESIÓN LINEAL POR MÍNIMOS CUADRADOS")
        print("=" * 55)

        print(f"Número de muestras: {len(x)}")
        print(f"Pendiente (m):     {m:.6f}")
        print(f"Intercepto (b):    {b:.6f}")

        print()
        print(f"Ecuación de la recta:")
        print(f"y = {m:.6f}x + {b:.6f}")

        print("=" * 55)

        # Mostrar la gráfica
        mostrar_grafica(x, y, m, b)

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{archivo}'.")

    except ValueError as error:
        print(f"Error en los datos: {error}")


if __name__ == "__main__":
    main()