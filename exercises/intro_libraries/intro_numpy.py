"""
📊 intro_numpy.py

Ejercicios prácticos para manipular arreglos y operaciones numéricas usando NumPy.
─────────────────────────────────────────────────────────────
🔧 Requisitos:
    - numpy
─────────────────────────────────────────────────────────────

autor: https://github.com/chucholoport
fecha: 11/09/2025
"""
# Librerías necesarias
import numpy as np


#########################################################################
# NOTE: Revisa la API de Numpy en https://numpy.org/doc/1.21/reference/ #
#########################################################################

# Ejercicio 1: Crear un arreglo de 10 ceros

#2


arg1 = np.zeros(10)
print(f"arreglo 1: {arg1}")

# Ejercicio 2: Crear un arreglo de números del 10 al 49

arg2 = np.arange(10, 50)
print(f"arreglo 2: {arg2}")

# Ejercicio 3: Invertir el arreglo anterior

arg3 = arg2[::-1]
print(f"arreglo 3: {arg3}")

# Ejercicio 4: Crear una matriz 3x3 con valores del 0 al 8


mat = np.arange(9).reshape(3, 3)
print(f"matriz:\n{mat}")

# Ejercicio 5: Encontrar índices de elementos mayores a 5


indices = np.where(mat > 5)
print(f"indices: {indices}")

# Ejercicio 6: Calcular la media, mediana y desviación estándar

mean = np.mean(arg2)
median = np.median(arg2)
std = np.std(arg2)
print(f"mean: {mean}, median: {median}, std: {std}")

# Ejercicio 7: Crear una matriz identidad de tamaño 4x4

identity = np.eye(4)
print(f"identity:\n{identity}")

# Ejercicio 8: Multiplicar dos matrices compatibles

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
product = np.dot(A, B)
print(f"product:\n{product}")

# Ejercicio 9: Normalizar un arreglo (valores entre 0 y 1)
# Función normalize
def normalize(val):
    return (val - val.min()) / (val.max() - val.min())

normalized = normalize(arg2)
print(f"normalized: {normalized}")

# Ejercicio 10: Crear un arreglo aleatorio de 100 elementos y contar cuántos están entre 0.3 y 0.7


np.random.seed(0)
random_array = np.random.rand(100)
count = np.sum(np.logical_and(random_array > 0.3, random_array < 0.7))
print(f"count: {count}")

# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué diferencia hay entre np.array y np.arange?
# - ¿Por qué es útil la matriz identidad en álgebra lineal?
# - ¿Qué significa normalizar un arreglo y cuándo se usa?

#si