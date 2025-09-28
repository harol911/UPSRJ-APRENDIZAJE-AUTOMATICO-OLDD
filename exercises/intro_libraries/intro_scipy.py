"""
intro_scipy.py

Ejercicios prácticos para resolver problemas numéricos y estadísticos usando SciPy.
─────────────────────────────────────────────────────────────
Requisitos:
    - numpy
    - scipy
─────────────────────────────────────────────────────────────
"""
# Librerías necesarias
import numpy as np
from scipy import linalg, stats, optimize, signal
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_scipy.log")

################################################################################
# NOTE: Revisa la API de SciPy en https://docs.scipy.org/doc//scipy/index.html #
################################################################################

# Ejercicio 1: Resolver un sistema lineal Ax = b
# 
# TODO: Define A y b como arreglos NumPy y encuentra x. Los valores son: A = [[3, 1], [1, 2]], b = [9, 8]
#
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
linear_system = linalg.solve(A, b)

# Impresion de la salida linear_system
plog(f"linear_system: {linear_system}", level=ERROR if linear_system is None else DEBUG, eol=True)

# Ejercicio 2: Calcular determinante y matriz inversa
#
# TODO: Obten el determinante y la inversa de la matriz A del ejercicio anterior
#
determinant = linalg.det(A)
inverse = linalg.inv(A)

# Impresion de la salida determinant e inverse
plog(f"determinant: {determinant}, inverse:\n{inverse}", level=ERROR if None in (determinant, inverse) else DEBUG, eol=True)

# Ejercicio 3: Estadísticas básicas sobre una muestraa
# 
# TODO: Obtén la media, desviación estándar y moda sobre un arreglo de datos [1, 2, 2, 3, 4, 4, 4, 5]
# 
data = np.array([1, 2, 2, 3, 4, 4, 4, 5])
mean = np.mean(data)
tstd = np.std(data, ddof=1)  # desviación estándar de la muestra
mode = stats.mode(data, keepdims=False)

# Impresion de la salida mean, tstd, mode
plog(f"media: {mean}, desviación estándar:\n{tstd}, moda:\n{mode}", level=ERROR if None in (mean, tstd, mode) else DEBUG, eol=True)

# Ejercicio 4: Ajuste de una función cuadrática
# 
# TODO: Encuentra el mínimo de una función f(x) = (x - 3)^2 + 2
#
def f(x):
    return (x - 3)**2 + 2

result = optimize.minimize_scalar(f)
f_min = result.x

# Impresion de la salida f_min
plog(f"Mínimo encontrado en x = {f_min}", level=ERROR if f_min is None else DEBUG, eol=True)

# Ejercicio 5: Transformada de Fourier de una señal
#
# TODO: Obten el espectro de una señal compuesta. Señal: sin(2π5t) + sin(2π20t)
#
t = np.linspace(0, 1, 500) # tiempo
# Crear la señal compuesta
signal_composite = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 20 * t)
# Obtener la transformada de Fourier
t_fourier = np.fft.fft(signal_composite)
# Obtener las frecuencias correspondientes
freqs = np.fft.fftfreq(len(t), t[1] - t[0])

# Impresion de la salida t_fourier
plog(f"F.T. = {np.abs(t_fourier[:10])}", level=ERROR if t_fourier is None else DEBUG, eol=True)

# Ejercicio 6: Filtrado de señal con Butterworth
#
# TODO: Usa signal.butter y signal.filtfilt para aplicar un filtro pasa-bajas. Nyquist = 0.5 * fs, low = 10 / Nyquist. Ruido: sin(2π5t) + 0.5sin(2π50t)")
#
fs = 100.0  # frecuencia de muestreo
# Crear la señal con ruido
t_filter = np.linspace(0, 1, int(fs))
signal_noisy = np.sin(2 * np.pi * 5 * t_filter) + 0.5 * np.sin(2 * np.pi * 50 * t_filter)
# Diseñar el filtro Butterworth
nyquist = 0.5 * fs
low = 10 / nyquist
b, a = signal.butter(5, low, btype='low')
# Aplicar el filtro
lp_filter = signal.filtfilt(b, a, signal_noisy)

# Impresion de la salida lp_filter
plog(f"Filtro Pasa-Bajas = {lp_filter[:10]}", level=ERROR if lp_filter is None else DEBUG, eol=True)

# 🧠 Preguntas interpretativas (responde en comentarios):
# 
# - ¿Qué representa la solución de Ax = b en términos geométricos?
# RESPUESTA: Geométricamente, resolver Ax = b representa encontrar el punto de intersección
# de dos rectas (en 2D) o planos (en 3D+). Cada ecuación del sistema representa una restricción
# geométrica, y la solución x es el punto que satisface todas las restricciones simultáneamente.
# 
# - ¿Por qué es útil conocer la moda y la desviación estándar de una muestra?
# RESPUESTA: La moda nos indica el valor más frecuente en los datos, útil para entender
# la tendencia central categórica. La desviación estándar mide la dispersión de los datos
# alrededor de la media, indicando qué tan "esparcidos" están los valores. Juntas nos dan
# información sobre la distribución y variabilidad de nuestros datos.
# 
# - ¿Qué información nos da la transformada de Fourier de una señal?
# RESPUESTA: La transformada de Fourier descompone una señal en sus componentes de frecuencia,
# mostrándonos qué frecuencias están presentes y con qué amplitud. Es como un "análisis espectral"
# que revela las oscilaciones ocultas en datos que parecen complejos en el dominio del tiempo.
# 
# - ¿Qué efecto tiene un filtro Butterworth sobre una señal compuesta?
# RESPUESTA: Un filtro Butterworth pasa-bajas elimina las componentes de alta frecuencia
# (ruido) mientras preserva las de baja frecuencia (señal útil). Tiene una respuesta
# suave sin ondulaciones en la banda de paso, proporcionando una transición gradual
# entre las frecuencias que pasan y las que se atenúan.