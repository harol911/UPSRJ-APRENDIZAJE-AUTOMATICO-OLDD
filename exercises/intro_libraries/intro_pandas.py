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
# Adjust the import path to include the parent directory for py_utils
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

# Ejercicio 1: Manejo de archivos CSV
#
# TODO: Cargar el archivo CSV y registrar la cantidad de registros.
#
csv_data = pd.read_csv(input_csv)
plog(f"CSV cargado correctamente. Registros: {len(csv_data)}", level=INFO)

# Impresion de la salida csv_data
plog(f"csv: {csv_data}", level=ERROR if csv_data is None else DEBUG, eol=True)

# Ejercicio 02: Manejo de archivos JSON
#
# TODO: Cargar el archivo JSON y registrar la cantidad de registros.
#
json_data = pd.read_json(input_json)
plog(f"JSON cargado correctamente. Registros: {len(json_data)}", level=INFO)

# Impresion de la salida json_data
plog(f"json: {json_data}", level=ERROR if json_data is None else DEBUG, eol=True)

# Ejercicio 03: Manejo de archivos YAML
#
# TODO: Cargar el archivo YAML y registrar la cantidad de registros.
#
with open(input_yaml, 'r', encoding='utf-8') as file:
    yaml_content = yaml.safe_load(file)
yaml_data = pd.DataFrame(yaml_content)
plog(f"YAML cargado correctamente. Registros: {len(yaml_data)}", level=INFO)

# Impresion de la salida yaml_data
plog(f"yaml: {yaml_data}", level=ERROR if yaml_data is None else DEBUG, eol=True)

# Ejercicio 04: Mostrar el encabezado del DataFrame
#
# TODO: Mostrar los primeros 5 registros del DataFrame.
#
df_head = csv_data.head(5)
plog(f"Primeros 5 registros mostrados", level=INFO)

# Impresion de la salida df_head
plog(f"DataFrame head: {df_head}", level=ERROR if df_head is None else DEBUG, eol=True)

# Ejercicio 05: Filtrado de información
#
# TODO: Filtrar estudiantes con promedio > 9.
#
above_nine = csv_data[csv_data['promedio'] > 9]
plog(f"Estudiantes con promedio > 9: {len(above_nine)} encontrados", level=INFO)

# Impresion de la salida above_nine
plog(f"Estudiantes con promedio > 9: {above_nine}", level=ERROR if above_nine is None else DEBUG, eol=True)

# Ejercicio 06: Agrupamiento y estadísticas
#
# TODO: Agrupar por carrera y calcular promedio general.
#
career_group = csv_data.groupby('carrera')['promedio'].mean()
general_mean = csv_data['promedio'].mean()
plog(f"Agrupamiento por carrera completado", level=INFO)

# Impresion de la salida career_group
plog(f"Promedio por carrera: {career_group}", level=ERROR if career_group is None else DEBUG, eol=True)

# Impresion de la salida general_mean
plog(f"Promedio general: {general_mean}", level=ERROR if general_mean is None else DEBUG, eol=True)

# Ejercicio 07: Conteo por categoría
#
# TODO: Contar estudiantes por género.
#
total_male = len(csv_data[csv_data['genero'] == 'M'])
total_female = len(csv_data[csv_data['genero'] == 'F'])
plog(f"Conteo por género completado", level=INFO)

# Impresion de la salida total_male
plog(f"Total hombres: {total_male}", level=ERROR if total_male is None else DEBUG, eol=True)

# Impresion de la salida total_female
plog(f"Total mujeres: {total_female}", level=ERROR if total_female is None else DEBUG, eol=True)
    
# Ejercicio 08: Exportar datos
#
# TODO: Exportar estudiantes con promedio > 9 (above_nine) a 'outputs/excelentes.csv, 
#       'outputs/excelentes.json' y 'outputs/excelentes.yaml'
#
# Crear directorio de salida si no existe
os.makedirs('outputs', exist_ok=True)

# Exportar a CSV
above_nine.to_csv('outputs/excelentes.csv', index=False)
plog(f"Datos exportados a outputs/excelentes.csv", level=INFO)

# Exportar a JSON
above_nine.to_json('outputs/excelentes.json', orient='records', indent=2)
plog(f"Datos exportados a outputs/excelentes.json", level=INFO)

# Exportar a YAML
yaml_output = above_nine.to_dict('records')
with open('outputs/excelentes.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(yaml_output, file, default_flow_style=False, allow_unicode=True)
plog(f"Datos exportados a outputs/excelentes.yaml", level=INFO)

# Ejercicio 09: Comparar formatos
# 
# TODO: Verificar que los tres formatos tengan el mismo número de registros.
# 
count_compare = {
    'CSV': len(csv_data),
    'JSON': len(json_data),
    'YAML': len(yaml_data)
}
plog(f"Comparación de registros completada", level=INFO)

# Verificar si todos tienen el mismo número de registros
all_equal = len(set(count_compare.values())) == 1
plog(f"Todos los formatos tienen el mismo número de registros: {all_equal}", level=INFO)

# Impresion de la salida count_compare
plog(f"Registros en CSV: {count_compare}", level=ERROR if count_compare is None else DEBUG, eol=True)