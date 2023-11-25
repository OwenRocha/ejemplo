# -*- coding: utf-8 -*-
"""limpiar_y_graficar

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PwW6QGO8JCPNYiYCWu6MxtVB9PTvFx48
"""

import pandas as pd
import matplotlib.pyplot as plt

def limpiar_y_graficar(dataset, columna_x, columna_y):
    # Convertir el dataset a un DataFrame de Pandas (si no lo es)
    df = pd.DataFrame(dataset)

    # Eliminar registros con valores vacíos en las columnas especificadas
    df_cleaned = df.dropna(subset=[columna_x, columna_y])

    # Imprimir el dataset limpio
    print("Dataset limpio:\n", df_cleaned)

    # Obtener datos de las columnas especificadas para el gráfico de dispersión
    data_x = df_cleaned[columna_x]
    data_y = df_cleaned[columna_y]

    # Crear el gráfico de dispersión
    plt.figure(figsize=(8, 6))
    plt.scatter(data_x, data_y, color='blue', marker='o', label='Datos')
    plt.title('Diagrama de Dispersión')
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.legend()
    plt.grid(True)

    plt.show()