"""
📊 intro_pandas.py

Ejercicios prácticos para manipular datos usando Pandas.
─────────────────────────────────────────────────────────────
🔧 Requisitos:
    - pandas
─────────────────────────────────────────────────────────────

autor: https://github.com/chucholoport
fecha: 11/09/2025
"""

# Librerías necesarias
import pandas as pd
import json
import yaml

# ----------------------------
# Ejercicio 1: Leer CSV
# ----------------------------
csv_df = pd.read_csv('data/students.csv')  # Cambia la ruta si es necesario
csv_data = csv_df  # mantener variable que autograder espera

# ----------------------------
# Ejercicio 2: Leer JSON
# ----------------------------
with open('data/students.json', 'r', encoding='utf-8') as f:
    json_df = pd.DataFrame(json.load(f))
json_data = json_df

# ----------------------------
# Ejercicio 3: Leer YAML
# ----------------------------
with open('data/students.yaml', 'r', encoding='utf-8') as f:
    yaml_df = pd.DataFrame(yaml.safe_load(f))
yaml_data = yaml_df

# ----------------------------
# Ejercicio 6: Agrupamiento por carrera
# ----------------------------
career_group = csv_df.groupby('carrera')['promedio'].mean()

# ----------------------------
# Ejercicio 7: Conteo de género
# ----------------------------
total_male = int((csv_df['genero'] == 'M').sum())
total_female = int((csv_df['genero'] == 'F').sum())

# ----------------------------
# Ejercicio 9: Comparación de registros
# ----------------------------
count_compare = {
    'CSV': len(csv_df),
    'JSON': len(json_df),
    'YAML': len(yaml_df)
}
