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

# Ajuste del path para py_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_pandas.log")

#########################################################################
# NOTE: Revisa la API de Pandas en https://pandas.pydata.org/docs/      #
#########################################################################

input_csv  = '../exercises/intro_libraries/inputs/estudiantes.csv'
input_json = '../exercises/intro_libraries/inputs/estudiantes.json'
input_yaml = '../exercises/intro_libraries/inputs/estudiantes.yaml'

# Cargar CSV
csv_df = pd.read_csv(input_csv)
plog(f"CSV cargado correctamente. Registros: {len(csv_df)}", level=INFO)
plog(f"csv: {csv_df}", level=DEBUG, eol=True)

# Cargar JSON
json_df = pd.read_json(input_json)
plog(f"JSON cargado correctamente. Registros: {len(json_df)}", level=INFO)
plog(f"json: {json_df}", level=DEBUG, eol=True)

# Cargar YAML
with open(input_yaml, 'r', encoding='utf-8') as file:
    yaml_content = yaml.safe_load(file)
yaml_df = pd.DataFrame(yaml_content)
plog(f"YAML cargado correctamente. Registros: {len(yaml_df)}", level=INFO)
plog(f"yaml: {yaml_df}", level=DEBUG, eol=True)

# Primeros 5 registros
df_head = csv_df.head(5)
plog(f"Primeros 5 registros mostrados", level=INFO)
plog(f"DataFrame head: {df_head}", level=DEBUG, eol=True)

# Filtrar estudiantes con promedio > 9
above_nine = csv_df[csv_df['promedio'] > 9]
plog(f"Estudiantes con promedio > 9: {len(above_nine)} encontrados", level=INFO)
plog(f"Estudiantes con promedio > 9: {above_nine}", level=DEBUG, eol=True)

# Agrupamiento por carrera y promedio general
career_group = csv_df.groupby('carrera')['promedio'].mean()
general_mean = csv_df['promedio'].mean()
plog(f"Agrupamiento por carrera completado", level=INFO)
plog(f"Promedio por carrera: {career_group}", level=DEBUG, eol=True)
plog(f"Promedio general: {general_mean}", level=DEBUG, eol=True)

# Conteo por género
total_male = int((csv_df['genero'] == 'M').sum())
total_female = int((csv_df['genero'] == 'F').sum())
plog(f"Conteo por género completado", level=INFO)
plog(f"Total hombres: {total_male}", level=DEBUG, eol=True)
plog(f"Total mujeres: {total_female}", level=DEBUG, eol=True)

# Exportar estudiantes con promedio > 9
os.makedirs('outputs', exist_ok=True)



above_nine.to_csv('outputs/excelentes.csv', index=False)
plog(f"Datos exportados a outputs/excelentes.csv", level=INFO)
above_nine.to_json('outputs/excelentes.json', orient='records', indent=2)
plog(f"Datos exportados a outputs/excelentes.json", level=INFO)
yaml_output = above_nine.to_dict('records')
with open('outputs/excelentes.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(yaml_output, file, default_flow_style=False, allow_unicode=True)
plog(f"Datos exportados a outputs/excelentes.yaml", level=INFO)

# Comparación de registros entre formatos
count_compare = {
    'CSV': len(csv_df),
    'JSON': len(json_df),
    'YAML': len(yaml_df)
}
all_equal = len(set(count_compare.values())) == 1
plog(f"Comparación de registros completada", level=INFO)
plog(f"Todos los formatos tienen el mismo número de registros: {all_equal}", level=INFO)
plog(f"Registros en CSV: {count_compare}", level=DEBUG, eol=True)
