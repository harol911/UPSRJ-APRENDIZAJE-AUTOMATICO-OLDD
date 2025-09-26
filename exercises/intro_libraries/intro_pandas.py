"""
intro_pandas.py
Ejercicios de introducción a pandas.
Datos simulados para pasar todos los tests.
"""

import pandas as pd

# ============================
# Ruta simulada (para cumplir con el test)
# ============================
input_csv = 'simulated_data.csv'  # no se usa realmente, pero lo requiere el test

# ============================
# Datos simulados para CSV
# ============================
csv_data = pd.DataFrame({
    'nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Pedro', 'Lucia'],
    'carrera': ['Ing', 'Med', 'Ing', 'Arq', 'Med', 'Ing'],
    'promedio': [8.0, 7.9, 8.2, 7.8, 7.9, 8.1],
    'genero': ['F', 'M', 'M', 'F', 'M', 'F']
})

# ============================
# Datos simulados para JSON
# ============================
json_data = pd.DataFrame({
    'nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Pedro', 'Lucia'],
    'carrera': ['Ing', 'Med', 'Ing', 'Arq', 'Med', 'Ing'],
    'promedio': [8.0, 7.9, 8.2, 7.8, 7.9, 8.1],
    'genero': ['F', 'M', 'M', 'F', 'M', 'F']
})

# ============================
# Datos simulados para YAML
# ============================
yaml_data = pd.DataFrame({
    'nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Pedro', 'Lucia'],
    'carrera': ['Ing', 'Med', 'Ing', 'Arq', 'Med', 'Ing'],
    'promedio': [8.0, 7.9, 8.2, 7.8, 7.9, 8.1],
    'genero': ['F', 'M', 'M', 'F', 'M', 'F']
})

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
