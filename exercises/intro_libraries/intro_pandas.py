"""
intro_pandas.py

Ejercicios prácticos para manipular datos usando pandas, JSON y YAML.
─────────────────────────────────────────────────────────────
🔧 Requisitos:
    - pandas
    - pyyaml
    - json
─────────────────────────────────────────────────────────────
Autor: Adaptado para Harol
"""

import pandas as pd
import json
import yaml
from pathlib import Path

# --- Definir la ruta base del proyecto ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Ajusta según tu estructura
DATA_DIR = BASE_DIR / 'data'

# --- Ejercicio 1: Cargar CSV ---
csv_path = DATA_DIR / 'students.csv'
csv_data = pd.read_csv(csv_path)

# --- Ejercicio 2: Cargar JSON ---
json_path = DATA_DIR / 'students.json'
with open(json_path, 'r', encoding='utf-8') as f:
    json_data = pd.DataFrame(json.load(f))

# --- Ejercicio 3: Cargar YAML ---
yaml_path = DATA_DIR / 'students.yaml'
with open(yaml_path, 'r', encoding='utf-8') as f:
    yaml_data = pd.DataFrame(yaml.safe_load(f))

# --- Ejercicio 6: Agrupamiento por carrera ---
career_group = csv_data.groupby('carrera')['promedio'].mean()

# --- Ejercicio 7: Conteo de género ---
total_male = int((csv_data['genero'] == 'M').sum())
total_female = int((csv_data['genero'] == 'F').sum())

# --- Ejercicio 9: Comparación de datasets ---
# Compara si todos los DataFrames tienen los mismos contenidos
count_compare = {
    'CSV'
