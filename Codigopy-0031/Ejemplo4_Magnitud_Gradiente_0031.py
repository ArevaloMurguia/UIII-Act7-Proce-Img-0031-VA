# ============================================================
# EJEMPLO 4: MAGNITUD DEL GRADIENTE
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

# Kernel Sobel Y
sobel_y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
], dtype=np.float32)

# Aplicar filtros
resultado_x = aplicar_filtro_frecuencia(
    imagen,
    sobel_x
)

resultado_y = aplicar_filtro_frecuencia(
    imagen,
    sobel_y
)

# Calcular magnitud del gradiente
magnitud = np.sqrt(
    resultado_x**2 + resultado_y**2
)

# Normalizar resultados
img_x = normalizar_visualizacion(resultado_x)
img_y = normalizar_visualizacion(resultado_y)
img_magnitud = normalizar_visualizacion(magnitud)

# Obtener espectros
espectro_x = obtener_espectro(resultado_x)
espectro_y = obtener_espectro(resultado_y)

# Crear figura de 6 imagenes
figura, ejes = plt.subplots(2, 3, figsize=(16, 10))

# Primera fila
ejes[0, 0].imshow(imagen, cmap="gray")
ejes[0, 0].set_title("1. Imagen Original")
ejes[0, 0].axis("off")

ejes[0, 1].imshow(espectro_x, cmap="gray")
ejes[0, 1].set_title("2. Espectro Sobel X")
ejes[0, 1].axis("off")

ejes[0, 2].imshow(espectro_y, cmap="gray")
ejes[0, 2].set_title("3. Espectro Sobel Y")
ejes[0, 2].axis("off")

# Segunda fila
ejes[1, 0].imshow(img_x, cmap="gray")
ejes[1, 0].set_title("4. Respuesta Sobel X")
ejes[1, 0].axis("off")

ejes[1, 1].imshow(img_y, cmap="gray")
ejes[1, 1].set_title("5. Respuesta Sobel Y")
ejes[1, 1].axis("off")

ejes[1, 2].imshow(img_magnitud, cmap="gray")
ejes[1, 2].set_title("6. Magnitud del Gradiente")
ejes[1, 2].axis("off")

plt.tight_layout()

# Guardar resultado
guardar_grafica(
    figura,
    "04_comparacion_magnitud_gradiente.png"
)

plt.show()

print("-*-*-*-*- Arevalo Rafael NC:0031 *-*-*-*-")