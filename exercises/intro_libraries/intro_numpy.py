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




arg1 = np.zeros(10)
print(f"arreglo 1: {arg1}")

# Ejercicio 2: Crear un arreglo de números del 10 al 49


arg2 = np.arange(10, 50)
print(f"arreglo 2: {arg2}")

# Ejercicio 3: Invertir el arreglo anterior


arg3 = arg2[::-1]
print(f"arreglo 3: {arg3}")

# Ejercicio 4: Crear una matriz 3x3 con valores del 0 al 8 (corregido)
# Nota: Para valores del 0 al 8, usamos np.arange(9)
# Si quisieras del 0 al 86, sería np.arange(87).reshape(3, 29) o una matriz más grande
mat = np.arange(9).reshape(3, 3)
print(f"matriz:\n{mat}")

# Ejercicio 5: Encontrar índices de elementos mayores a 5



indices = np.where(mat > 5)
print(f"indices: {indices}")
# Alternativa más legible: obtener los valores también
elementos_mayores = mat[mat > 5]
print(f"elementos mayores a 5: {elementos_mayores}")

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
# Dos formas de multiplicar matrices:
product_dot = np.dot(A, B)  # Multiplicación matricial
product_at = A @ B          # Operador @ (más moderno)
print(f"product (dot):\n{product_dot}")
print(f"product (@):\n{product_at}")

# Ejercicio 9: Normalizar un arreglo (valores entre 0 y 1)




def normalize(val):
    """Normaliza un arreglo para que sus valores estén entre 0 y 1"""
    return (val - val.min()) / (val.max() - val.min())

normalized = normalize(arg2)
print(f"normalized: {normalized}")
print(f"min: {normalized.min()}, max: {normalized.max()}")

# Ejercicio 10: Crear un arreglo aleatorio de 100 elementos y contar cuántos están entre 0.3 y 0.7
np.random.seed(0)  # Para reproducibilidad
random_array = np.random.rand(100)
count = np.sum(np.logical_and(random_array > 0.3, random_array < 0.7))
# Alternativa más simple:
count_alt = np.sum((random_array > 0.3) & (random_array < 0.7))
print(f"count: {count}")
print(f"count alternativo: {count_alt}")

# Ejercicios adicionales de práctica:
print("\n" + "="*50)
print("EJERCICIOS ADICIONALES")
print("="*50)

# Ejercicio 11: Crear una matriz 5x5 con valores aleatorios y encontrar min/max
random_matrix = np.random.rand(5, 5)
print(f"Matriz aleatoria 5x5:\n{random_matrix}")
print(f"Valor mínimo: {random_matrix.min()}")
print(f"Valor máximo: {random_matrix.max()}")
print(f"Posición del mínimo: {np.unravel_index(random_matrix.argmin(), random_matrix.shape)}")

# Ejercicio 12: Operaciones elemento a elemento
arr_a = np.array([1, 2, 3, 4, 5])
arr_b = np.array([2, 2, 2, 2, 2])
print(f"Suma: {arr_a + arr_b}")
print(f"Multiplicación: {arr_a * arr_b}")
print(f"Potencia: {arr_a ** arr_b}")

# 🧠 RESPUESTAS A LAS PREGUNTAS INTERPRETATIVAS:

"""
❓ ¿Qué diferencia hay entre np.array y np.arange?

🔹 np.array(): Crea un arreglo a partir de una lista o secuencia existente
   Ejemplo: np.array([1, 2, 3, 4])
   
🔹 np.arange(): Crea un arreglo con una secuencia de números en un rango
   Ejemplo: np.arange(1, 5) → [1, 2, 3, 4]
   Similar a range() de Python pero devuelve un arreglo NumPy

❓ ¿Por qué es útil la matriz identidad en álgebra lineal?

🔹 La matriz identidad (I) es el elemento neutro de la multiplicación matricial
🔹 Para cualquier matriz A: A × I = I × A = A
🔹 Es fundamental para:
   - Resolver sistemas de ecuaciones lineales
   - Calcular matrices inversas (A × A⁻¹ = I)
   - Transformaciones lineales
   - Eigenvalores y eigenvectores

❓ ¿Qué significa normalizar un arreglo y cuándo se usa?

🔹 Normalizar significa escalar los valores para que estén en un rango específico (0-1)
🔹 Fórmula: (valor - mínimo) / (máximo - mínimo)
🔹 Se usa en:
   - Machine Learning (para que todas las características tengan la misma escala)
   - Procesamiento de imágenes (píxeles entre 0-1)
   - Análisis de datos (comparar variables con diferentes unidades)
   - Redes neuronales (mejora la convergencia del entrenamiento)
"""

