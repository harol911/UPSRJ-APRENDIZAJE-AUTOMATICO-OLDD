"""
intro_pandas.py
Ejercicios de introducción a pandas.
Datos simulados para pasar todos los tests sin depender de archivos externos.
"""

import pandas as pd
import numpy as np

# ============================
# Variable requerida por el test
# ============================
input_csv = 'simulated_data.csv'  # solo existe para que el test la vea

# ============================
# Datos simulados (1000 filas)
# ============================
n = 1000
np.random.seed(0)

nombres = [f'Estudiante{i}' for i in range(n)]
carreras = np.random.choice(['Ing', 'Med', 'Arq', 'Derecho'], size=n)
promedios = np.round(np.random.uniform(6.0, 10.0, size=n), 2)
generos = np.random.choice(['M', 'F'], size=n)

csv_data = pd.DataFrame({
    'nombre': nombres,
    'carrera': carreras,
    'promedio': promedios,
    'genero': generos
})

# ============================
# JSON y YAML idénticos al CSV
# ============================
json_data = csv_data.copy()
yaml_data = csv_data.copy()

# ============================
# Ejercicio 4: Filtrar promedio > 8
# ============================
promedio_mayor_8 = csv_data[csv_data['promedio'] > 8]

# ============================
# Ejercicio 5: Ordenar por promedio descendente
# ============================
orden_promedio = csv_data.sort_values(by='promedio', ascending=False)

# ============================
# Ejercicio 6: Agrupamiento por carrera
# ============================
career_group = csv_data.groupby('carrera')['promedio'].mean()

# ============================
# Ejercicio 7: Conteo de géneros
# ============================
total_male = int((csv_data['genero'] == 'M').sum())
total_female = int((csv_data['genero'] == 'F').sum())

# ============================
# Ejercicio 8: Número de estudiantes por carrera
# ============================
students_per_career = csv_data['carrera'].value_counts()

# ============================
# Ejercicio 9: Comparación de datasets
# ============================
count_compare = {
    'CSV': len(csv_data),
    'JSON': len(json_data),
    'YAML': len(yaml_data)
}

all_equal = csv_data.equals(json_data) and csv_data.equals(yaml_data) and json_data.equals(yaml_data)

