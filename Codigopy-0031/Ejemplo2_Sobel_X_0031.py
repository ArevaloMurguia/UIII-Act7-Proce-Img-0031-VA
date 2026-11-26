# ============================================================
# EJEMPLO 2: FILTRO SOBEL X
# ALUMNO: AREVALO RAFAEL
# NC: 0031
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

from Funciones_Frecuencia_0031 import (
    cargar_imagen,
    obtener_espectro,
    aplicar_filtro_frecuencia,
    normalizar_visualizacion,
    guardar_grafica
)

# Cargar imagen
imagen = cargar_imagen()

# Kernel Sobel X
sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype=np.float32)

# Aplicar filtro
resultado_x = aplicar_filtro_frecuencia(
    imagen,
    sobel_x
)

# Obtener espectro
espectro_x = obtener_espectro(resultado_x)

# Normalizar resultado
imagen_x = normalizar_visualizacion(resultado_x)

# Crear graficas
figura, ejes = plt.subplots(1, 3, figsize=(15, 5))

ejes[0].imshow(imagen, cmap="gray")
ejes[0].set_title("Imagen Original")
ejes[0].axis("off")

ejes[1].imshow(espectro_x, cmap="gray")
ejes[1].set_title("Espectro Sobel X")
ejes[1].axis("off")

ejes[2].imshow(imagen_x, cmap="gray")
ejes[2].set_title("Sobel X: Bordes Verticales")
ejes[2].axis("off")

plt.tight_layout()

# Guardar resultado
guardar_grafica(
    figura,
    "02_sobel_x.png"
)

plt.show()

print("-*-*-*-*-*-*- Arevalo Rafael NC:0031 *-*-*-*-*-*-")