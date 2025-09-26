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

input_csv  = '../exercises/intro_libraries/inputs/estudiantes.csv'
input_json = '../exercises/intro_libraries/inputs/estudiantes.json'
input_yaml = '../exercises/intro_libraries/inputs/estudiantes.yaml'

# Cargar los DataFrames completos
csv_df = pd.read_csv(input_csv)
json_df = pd.read_json(input_json)
with open(input_yaml, 'r', encoding='utf-8') as file:
    yaml_content = yaml.safe_load(file)
yaml_df = pd.DataFrame(yaml_content)

# ----------------- Ejercicios 1,2,3: contar registros -----------------
csv_data = len(csv_df)
json_data = len(json_df)
yaml_data = len(yaml_df)

plog(f"CSV cargado correctamente. Registros: {csv_data}", level=INFO)
plog(f"JSON cargado correctamente. Registros: {json_data}", level=INFO)
plog(f"YAML cargado correctamente. Registros: {yaml_data}", level=INFO)

# ----------------- Ejercicio 4: mostrar encabezado -----------------
df_head = csv_df.head(5)
plog(f"Primeros 5 registros mostrados", level=INFO)
plog(f"DataFrame head: {df_head}", level=DEBUG, eol=True)

# ----------------- Ejercicio 5: filtrar estudiantes con promedio > 9 -----------------
above_nine = csv_df[csv_df['promedio'] > 9]
plog(f"Estudiantes con promedio > 9: {len(above_nine)} encontrados", level=INFO)
plog(f"Estudiantes con promedio > 9: {above_nine}", level=DEBUG, eol=True)

# ----------------- Ejercicio 6: Agrupamiento por carrera y promedio general -----------------
career_group = csv_df.groupby('carrera')['promedio'].mean()
general_mean = csv_df['promedio'].mean()
plog(f"Agrupamiento por carrera completado", level=INFO)
plog(f"Promedio por carrera: {career_group}", level=DEBUG, eol=True)
plog(f"Promedio general: {general_mean}", level=DEBUG, eol=True)

# ----------------- Ejercicio 7: Conteo por género -----------------
total_male = int((csv_df['genero'] == 'M').sum())
total_female = int((csv_df['genero'] == 'F').sum())
plog(f"Conteo por género completado", level=INFO)
plog(f"Total hombres: {total_male}", level=DEBUG, eol=True)
plog(f"Total mujeres: {total_female}", level=DEBUG, eol=True)

# ----------------- Ejercicio 8: Exportar estudiantes con promedio > 9 -----------------
os.makedirs('outputs', exist_ok=True)



above_nine.to_csv('outputs/excelentes.csv', index=False)







above_nine.to_json('outputs/excelentes.json', orient='records', indent=2)







with open('outputs/excelentes.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(above_nine.to_dict('records'), file, default_flow_style=False, allow_unicode=True)
plog(f"Datos exportados a outputs/", level=INFO)

# ----------------- Ejercicio 9: Comparar formatos -----------------
count_compare = csv_df.equals(json_df) and csv_df.equals(yaml_df) and json_df.equals(yaml_df)
plog(f"Todos los formatos tienen el mismo contenido: {count_compare}", level=INFO)
