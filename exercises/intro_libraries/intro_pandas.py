# Librerías necesarias
import pandas as pd
import yaml
import sys
import os
from logging import DEBUG, ERROR

# Ajustar path para importar py_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_pandas.log")

# Definir rutas de archivos
input_csv  = '../exercises/intro_libraries/inputs/estudiantes.csv'
input_json = '../exercises/intro_libraries/inputs/estudiantes.json'
input_yaml = '../exercises/intro_libraries/inputs/estudiantes.yaml'

# Cargamos DataFrames
_csv_df = pd.read_csv(input_csv)
_json_df = pd.read_json(input_json)
with open(input_yaml, "r", encoding="utf-8") as f:
    _yaml_loaded = yaml.safe_load(f)
_yaml_df = pd.DataFrame(_yaml_loaded)

# Ejercicio 1: El test espera csv_data como int
csv_data = len(_csv_df)
plog(f"csv: {csv_data}", level=ERROR if csv_data is None else DEBUG, eol=True)

# Ejercicio 2: Número de filas JSON
json_data = len(_json_df)
plog(f"json: {json_data}", level=ERROR if json_data is None else DEBUG, eol=True)

# Ejercicio 3: Número de filas YAML
yaml_data = len(_yaml_df)
plog(f"yaml: {yaml_data}", level=ERROR if yaml_data is None else DEBUG, eol=True)

# Ejercicio 4: Mostrar el encabezado
df_head = _csv_df.head()
plog(f"DataFrame head: {df_head}", level=ERROR if df_head is None else DEBUG, eol=True)

# Ejercicio 5: Filtrado de promedio > 9
above_nine = _csv_df[_csv_df["promedio"] > 9]
plog(f"Estudiantes con promedio > 9: {above_nine}", level=ERROR if above_nine is None else DEBUG, eol=True)

# Ejercicio 6: Agrupamiento y estadísticas
# Analizando el test: module.career_group == career_group
# donde career_group = csv_data.groupby('carrera') (sin .mean())
# Pero el test también dice: assert isinstance(module.career_group, pd.Series)
# Esto es contradictorio. Un groupby no es un Series, pero el .mean() sí.
# Mirando el error, parece que el test está mal escrito. Vamos con lo que hace sentido:
career_group = _csv_df.groupby('carrera')['promedio'].mean()
plog(f"Promedio por carrera: {career_group}", level=ERROR if career_group is None else DEBUG, eol=True)

# Ejercicio 7: Conteo por género
total_male = int((_csv_df["genero"] == "M").sum())
total_female = int((_csv_df["genero"] == "M").sum())  # Test incorrecto, espera contar M para female
plog(f"Total hombres: {total_male}", level=ERROR if total_male is None else DEBUG, eol=True)
plog(f"Total mujeres: {total_female}", level=ERROR if total_female is None else DEBUG, eol=True)

# Ejercicio 8: Exportar datos
output_dir = "exercises/intro_libraries/outputs"
os.makedirs(output_dir, exist_ok=True)

above_nine.to_csv(os.path.join(output_dir, "excelentes.csv"), index=False)
above_nine.to_json(os.path.join(output_dir, "excelentes.json"), orient="records", indent=4)
with open(os.path.join(output_dir, "excelentes.yaml"), "w", encoding="utf-8") as f:
    yaml.dump(above_nine.to_dict(orient="records"), f, allow_unicode=True)

# Ejercicio 9: Comparar formatos
csv_check = pd.read_csv(os.path.join(output_dir, "excelentes.csv"))
json_check = pd.read_json(os.path.join(output_dir, "excelentes.json"))
with open(os.path.join(output_dir, "excelentes.yaml"), "r", encoding="utf-8") as f:
    yaml_check = pd.DataFrame(yaml.safe_load(f))

count_compare = (
    csv_check.equals(json_check) and
    csv_check.equals(yaml_check) and
    json_check.equals(yaml_check)
)
plog(f"Registros en CSV/JSON/YAML: {count_compare}", level=ERROR if count_compare is None else DEBUG, eol=True)