# ============================================================
# EJEMPLO 3: FILTRO SOBEL Y
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

# Kernel Sobel Y
sobel_y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
], dtype=np.float32)

# Aplicar filtro
resultado_y = aplicar_filtro_frecuencia(
    imagen,
    sobel_y
)

# Obtener espectro
espectro_y = obtener_espectro(resultado_y)

# Normalizar resultado
imagen_y = normalizar_visualizacion(resultado_y)

# Crear graficas
figura, ejes = plt.subplots(1, 3, figsize=(15, 5))

ejes[0].imshow(imagen, cmap="gray")
ejes[0].set_title("Imagen Original")
ejes[0].axis("off")

ejes[1].imshow(espectro_y, cmap="gray")
ejes[1].set_title("Espectro Sobel Y")
ejes[1].axis("off")

ejes[2].imshow(imagen_y, cmap="gray")
ejes[2].set_title("Sobel Y: Bordes Horizontales")
ejes[2].axis("off")

plt.tight_layout()

# Guardar resultado
guardar_grafica(
    figura,
    "03_sobel_y.png"
)

plt.show()

print("-*-*-*-* Arevalo Rafael NC:0031 -*-*-*-*-*-")