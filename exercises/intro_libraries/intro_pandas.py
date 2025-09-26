"""
intro_pandas.py

Ejercicios prácticos para manipular datos de estudiantes usando Pandas.
─────────────────────────────────────────────────────────────
Requisitos:
    - pandas
    - pyyaml
─────────────────────────────────────────────────────────────
"""
import pandas as pd
import yaml
import sys
import os
from logging import DEBUG, INFO

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_pandas.log")

input_csv  = '../exercises/intro_libraries/inputs/estudiantes.csv'
input_json = '../exercises/intro_libraries/inputs/estudiantes.json'
input_yaml = '../exercises/intro_libraries/inputs/estudiantes.yaml'

# ---------------- EJERCICIO 1 ----------------
csv_df = pd.read_csv(input_csv)
csv_data = len(csv_df)  # cantidad de registros
plog(f"CSV cargado correctamente. Registros: {csv_data}", level=INFO)

# ---------------- EJERCICIO 2 ----------------
json_df = pd.read_json(input_json)
json_data = len(json_df)
plog(f"JSON cargado correctamente. Registros: {json_data}", level=INFO)

# ---------------- EJERCICIO 3 ----------------
with open(input_yaml, 'r', encoding='utf-8') as file:
    yaml_content = yaml.safe_load(file)
yaml_df = pd.DataFrame(yaml_content)
yaml_data = len(yaml_df)
plog(f"YAML cargado correctamente. Registros: {yaml_data}", level=INFO)

# ---------------- EJERCICIO 4 ----------------
df_head = csv_df.head(5)
plog(f"Primeros 5 registros mostrados", level=INFO)
plog(f"DataFrame head: {df_head}", level=DEBUG, eol=True)

# ---------------- EJERCICIO 5 ----------------
above_nine = csv_df[csv_df['promedio'] > 9]
plog(f"Estudiantes con promedio > 9: {len(above_nine)} encontrados", level=INFO)

# ---------------- EJERCICIO 6 ----------------
career_group = csv_df.groupby('carrera')['promedio'].mean()
general_mean = csv_df['promedio'].mean()
plog(f"Agrupamiento por carrera completado", level=INFO)

# ---------------- EJERCICIO 7 ----------------
total_male = int((csv_df['genero'] == 'M').sum())
total_female = int((csv_df['genero'] == 'F').sum())
plog(f"Conteo por género completado", level=INFO)

# ---------------- EJERCICIO 8 ----------------
os.makedirs('outputs', exist_ok=True)
above_nine.to_csv('outputs/excelentes.csv', index=False)
above_nine.to_json('outputs/excelentes.json', orient='records', indent=2)
with open('outputs/excelentes.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(above_nine.to_dict('records'), file, default_flow_style=False, allow_unicode=True)

# ---------------- EJERCICIO 9 ----------------
count_compare = (csv_data == json_data == yaml_data)
plog(f"Comparación de registros completada: {count_compare}", level=INFO)
