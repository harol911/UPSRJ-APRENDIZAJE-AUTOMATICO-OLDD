"""
📊 intro_pandas.py

Ejercicios prácticos para manipular datos de estudiantes usando Pandas.
─────────────────────────────────────────────────────────────
Requisitos:
    - pandas
    - pyyaml
─────────────────────────────────────────────────────────────
"""

import pandas as pd
import yaml
import os
from logging import DEBUG, WARNING

# Logger
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_pandas.log")
os.makedirs('outputs', exist_ok=True)


# ------------------- Funciones de lectura -------------------
def read_csv(path):
    if os.path.exists(path):
        df = pd.read_csv(path)
        plog(f"CSV: {len(df)} registros", level=DEBUG, eol=True)
        return df
    plog(f"Archivo CSV no encontrado: {path}. Usando datos de prueba.", level=WARNING, eol=True)
    return pd.DataFrame([
        {"nombre": "Test1", "carrera": "Ing", "promedio": 10, "genero": "M"},
        {"nombre": "Test2", "carrera": "Med", "promedio": 8, "genero": "F"}
    ])


def read_json(path):
    if os.path.exists(path):
        df = pd.read_json(path)
        plog(f"JSON: {len(df)} registros", level=DEBUG, eol=True)
        return df
    plog(f"Archivo JSON no encontrado: {path}. Usando datos de prueba.", level=WARNING, eol=True)
    return pd.DataFrame([
        {"nombre": "Test1", "carrera": "Ing", "promedio": 10, "genero": "M"},
        {"nombre": "Test2", "carrera": "Med", "promedio": 8, "genero": "F"}
    ])


def read_yaml(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        df = pd.DataFrame(data)
        plog(f"YAML: {len(df)} registros", level=DEBUG, eol=True)
        return df
    plog(f"Archivo YAML no encontrado: {path}. Usando datos de prueba.", level=WARNING, eol=True)
    return pd.DataFrame([
        {"nombre": "Test1", "carrera": "Ing", "promedio": 10, "genero": "M"},
        {"nombre": "Test2", "carrera": "Med", "promedio": 8, "genero": "F"}
    ])


# ------------------- Funciones de procesamiento -------------------
def summarize(df):
    if df.empty:
        plog("No hay datos para resumir.", level=WARNING, eol=True)
        return

    plog(f"DataFrame head:\n{df.head(5)}", level=DEBUG, eol=True)

    career_group = df.groupby('carrera')['promedio'].mean()
    general_mean = df['promedio'].mean()
    plog(f"Promedio por carrera:\n{career_group}", level=DEBUG, eol=True)
    plog(f"Promedio general: {general_mean}", level=DEBUG, eol=True)

    total_male = df[df['genero'] == 'M'].shape[0]
    total_female = df[df['genero'] == 'F'].shape[0]
    plog(f"Total hombres: {total_male}", level=DEBUG, eol=True)
    plog(f"Total mujeres: {total_female}", level=DEBUG, eol=True)


def export_above_nine(df, folder='outputs'):
    above_nine = df[df['promedio'] > 9]
    os.makedirs(folder, exist_ok=True)
    above_nine.to_csv(f'{folder}/excelentes.csv', index=False)
    above_nine.to_json(f'{folder}/excelentes.json', orient='records', force_ascii=False)
    with open(f'{folder}/excelentes.yaml', 'w', encoding='utf-8') as f:
        yaml.safe_dump(above_nine.to_dict(orient='records'), f, allow_unicode=True)
    plog(f"Exportados {len(above_nine)} registros con promedio > 9", level=DEBUG, eol=True)
    return above_nine


# ------------------- Función principal -------------------
def main():
    input_csv = 'outputs/estudiantes.csv'
    input_json = 'outputs/estudiantes.json'
    input_yaml = 'outputs/estudiantes.yaml'

    csv_data = read_csv(input_csv)
    json_data = read_json(input_json)
    yaml_data = read_yaml(input_yaml)

    summarize(csv_data)
    export_above_nine(csv_data)


if __name__ == "__main__":
    main()
