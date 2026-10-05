"""
Módulo para la lectura y validación de datos.
"""

import csv


def leer_datos(archivo):
    """
    Lee un archivo CSV que contiene dos columnas:

        x,y

    Devuelve dos listas:
        valores_x
        valores_y
    """

    valores_x = []
    valores_y = []

    with open(
        archivo,
        "r",
        newline="",
        encoding="utf-8-sig"
    ) as archivo_csv:

        lector = csv.reader(archivo_csv)

        for numero_linea, fila in enumerate(lector, start=1):

            # Ignorar líneas vacías
            if not fila or all(
                not dato.strip() for dato in fila
            ):
                continue

            # Verificar que existan dos columnas
            if len(fila) < 2:
                raise ValueError(
                    f"La línea {numero_linea} debe contener "
                    "dos valores: x,y."
                )

            try:
                x = float(fila[0].strip())
                y = float(fila[1].strip())

            except ValueError:

                # Permitir encabezados como:
                # x,y
                if numero_linea == 1:
                    continue

                raise ValueError(
                    f"Los valores de la línea "
                    f"{numero_linea} deben ser numéricos."
                )

            valores_x.append(x)
            valores_y.append(y)

    # Verificar cantidad mínima de datos
    if len(valores_x) < 2:
        raise ValueError(
            "Se necesitan al menos dos muestras."
        )

    return valores_x, valores_y