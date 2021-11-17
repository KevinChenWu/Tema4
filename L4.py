#!/usr/bin/env python
# coding: utf-8

# Mariana Chung B92250 / Kevin Chen Wu B92215
# Solucion problema 4, E13 Procesos aleatorios.

# Los parámetros T, t_final y N son elegidos arbitrariamente

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Variables aleatorias C y Z
vaC = stats.norm(5, np.sqrt(0.2))
vaZ = stats.uniform(0, np.pi/2)

# Creación del vector de tiempo
T = 100         # número de elementos
t_final = 10     # tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 20
X_t = np.empty((N, len(t)))    # N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso X(t) (C y Z independientes)
# Se eligio la constante ω, como π.

for i in range(N):
    C = vaC.rvs()
    Z = vaZ.rvs()
    x_t = C * np.cos(np.pi*t + Z)
    X_t[i, :] = x_t
    plt.plot(t, x_t)

# Promedio de las N realizaciones en cada instante (cada punto en t)

P = [np.mean(X_t[:, i]) for i in range(len(t))]
plt.plot(t, P, lw=6)

# Graficar el resultado teórico del valor esperado
E = 10/np.pi * (np.cos(np.pi*t) - np.sin(np.pi*t))
plt.plot(t, E, '-.', lw=4)

# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.show()

# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones
corr = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelación
plt.figure()

# Se crea de nuevo el proceso X(t) con Ω y Θ como constantes
# Se eligió la constante ω, como π.
# Se eligió la constante θ, como 0.

for i in range(N):
    C = vaC.rvs()
    x_t = C * np.cos(np.pi*t + 0)
    X_t[i, :] = x_t

# Cálculo de correlación para cada valor de tau
for n in range(N):
    for i, tau in enumerate(desplazamiento):
        corr[n, i] = np.correlate(X_t[n, :], np.roll(X_t[n, :], tau))/T
    plt.plot(taus, corr[n, :])

# Valor teórico de correlación
Rxx = 25.2 * np.cos(np.pi*t + 0) * np.cos(np.pi * (t + taus) + 0)

# Gráficas de correlación para cada realización y la
plt.plot(taus, Rxx, '-.', lw=4, label='Correlación teórica')
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{XX}(\tau)$')
plt.legend()
plt.show()
