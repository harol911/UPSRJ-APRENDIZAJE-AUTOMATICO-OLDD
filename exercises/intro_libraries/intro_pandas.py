"""
intro_pandas.py

Ejercicios prácticos para manipular datos de estudiantes usando Pandas.
─────────────────────────────────────────────────────────────
Requisitos:
    - pandas
    - pyyaml
─────────────────────────────────────────────────────────────
"""
# Librerías necesarias
import pandas as pd
import yaml
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_pandas.log")

#########################################################################
# NOTE: Revisa la API de Pandas en https://pandas.pydata.org/docs/      #
#########################################################################

# Archivos de entrada
input_csv  = 'inputs/estudiantes.csv'
input_json = 'inputs/estudiantes.json'
input_yaml = 'inputs/estudiantes.yaml'

# ---------------------- Generar datos simulados si no existen ----------------------
if not os.path.exists(input_csv):
    os.makedirs('inputs', exist_ok=True)
    df_sim = pd.DataFrame({
        'nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Jorge'],
        'carrera': ['Ing', 'Med', 'Derecho', 'Ing', 'Med'],
        'promedio': [9.5, 8.2, 9.8, 7.5, 10.0],
        'genero': ['F', 'M', 'M', 'F', 'M']
    })
    df_sim.to_csv(input_csv, index=False)
    df_sim.to_json(input_json, orient='records', force_ascii=False)
    with open(input_yaml, 'w', encoding='utf-8') as f:
        yaml.safe_dump(df_sim.to_dict(orient='records'), f, allow_unicode=True)

# ---------------------- Ejercicio 1: Manejo de archivos CSV ----------------------
csv_data = pd.read_csv(input_csv)
plog(f"csv: {len(csv_data)} registros", level=DEBUG, eol=True)

# ---------------------- Ejercicio 02: Manejo de archivos JSON ----------------------
json_data = pd.read_json(input_json)
plog(f"json: {len(json_data)} registros", level=DEBUG, eol=True)

# ---------------------- Ejercicio 03: Manejo de archivos YAML ----------------------
with open(input_yaml, 'r', encoding='utf-8') as f:
    yaml_dict = yaml.safe_load(f)
yaml_data = pd.DataFrame(yaml_dict)
plog(f"yaml: {len(yaml_data)} registros", level=DEBUG, eol=True)

# ---------------------- Ejercicio 04: Mostrar el encabezado del DataFrame ----------------------
df_head = csv_data.head(5)
plog(f"DataFrame head:\n{df_head}", level=DEBUG, eol=True)

# ---------------------- Ejercicio 05: Filtrado de información ----------------------
above_nine = csv_data[csv_data['promedio'] > 9]
plog(f"Estudiantes con promedio > 9:\n{above_nine}", level=DEBUG, eol=True)

# ---------------------- Ejercicio 06: Agrupamiento y estadísticas ----------------------
career_group = csv_data.groupby('carrera')['promedio'].mean()
general_mean = csv_data['promedio'].mean()
plog(f"Promedio por carrera:\n{career_group}", level=DEBUG, eol=True)
plog(f"Promedio general: {general_mean}", level=DEBUG, eol=True)

# ---------------------- Ejercicio 07: Conteo por categoría ----------------------
total_male = csv_data[csv_data['genero'] == 'M'].shape[0]
total_female = csv_data[csv_data['genero'] == 'F'].shape[0]
plog(f"Total hombres: {total_male}", level=DEBUG, eol=True)
plog(f"Total mujeres: {total_female}", level=DEBUG, eol=True)

# ---------------------- Ejercicio 08: Exportar datos ----------------------
os.makedirs('outputs', exist_ok=True)
above_nine.to_csv('outputs/excelentes.csv', index=False)
above_nine.to_json('outputs/excelentes.json', orient='records', force_ascii=False)
with open('outputs/excelentes.yaml', 'w', encoding='utf-8') as f:
    yaml.safe_dump(above_nine.to_dict(orient='records'), f, allow_unicode=True)

# ---------------------- Ejercicio 09: Comparar formatos ----------------------
count_csv = len(pd.read_csv('outputs/excelentes.csv'))
count_json = len(pd.read_json('outputs/excelentes.json'))
with open('outputs/excelentes.yaml', 'r', encoding='utf-8') as f:
    count_yaml = len(yaml.safe_load(f))
count_compare = (count_csv, count_json, count_yaml)
plog(f"Registros en CSV, JSON, YAML: {count_compare}", level=DEBUG, eol=True)


