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
from logging import DEBUG, INFO, WARNING, ERROR

# Asegurarse de poder importar py_utils
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_pandas.log")
os.makedirs('outputs', exist_ok=True)


def read_csv(path):
    if os.path.exists(path):
        df = pd.read_csv(path)
        plog(f"CSV: {len(df)} registros", level=DEBUG, eol=True)
        return df
    else:
        plog(f"Archivo CSV no encontrado: {path}", level=ERROR, eol=True)
        return pd.DataFrame()


def read_json(path):
    if os.path.exists(path):
        df = pd.read_json(path)
        plog(f"JSON: {len(df)} registros", level=DEBUG, eol=True)
        return df
    else:
        plog(f"Archivo JSON no encontrado: {path}", level=ERROR, eol=True)
        return pd.DataFrame()


def read_yaml(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        df = pd.DataFrame(data)
        plog(f"YAML: {len(df)} registros", level=DEBUG, eol=True)
        return df
    else:
        plog(f"Archivo YAML no encontrado: {path}", level=ERROR, eol=True)
        return pd.DataFrame()


def export_above_nine(df):
    above_nine = df[df['promedio'] > 9]
    above_nine.to_csv('outputs/excelentes.csv', index=False)
    above_nine.to_json('outputs/excelentes.json', orient='records', force_ascii=False)
    with open('outputs/excelentes.yaml', 'w', encoding='utf-8') as f:
        yaml.safe_dump(above_nine.to_dict(orient='records'), f, allow_unicode=True)
    plog(f"Exportados {len(above_nine)} registros con promedio > 9", level=DEBUG, eol=True)
    return above_nine


def summarize(df):
    if df.empty:
        plog("No hay datos para resumir.", level=WARNING, eol=True)
        return

    df_head = df.head(5)
    plog(f"DataFrame head:\n{df_head}", level=DEBUG, eol=True)

    career_group = df.groupby('carrera')['promedio'].mean()
    general_mean = df['promedio'].mean()
    plog(f"Promedio por carrera:\n{career_group}", level=DEBUG, eol=True)
    plog(f"Promedio general: {general_mean}", level=DEBUG, eol=True)

    total_male = df[df['genero'] == 'M'].shape[0]
    total_female = df[df['genero'] == 'F'].shape[0]
    plog(f"Total hombres: {total_male}", level=DEBUG, eol=True)
    plog(f"Total mujeres: {total_female}", level=DEBUG, eol=True)


# Función principal para ejecutar todo
def main():
    input_csv = 'outputs/estudiantes.csv'
    input_json = 'outputs/estudiantes.json'
    input_yaml = 'outputs/estudiantes.yaml'

    csv_data = read_csv(input_csv)
    json_data = read_json(input_json)
    yaml_data = read_yaml(input_yaml)

    summarize(csv_data)
    export_above_nine(csv_data)


# Solo ejecutar main si se llama directamente
if __name__ == "__main__":
    main()
