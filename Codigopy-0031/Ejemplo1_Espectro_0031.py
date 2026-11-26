# ============================================================
# EJEMPLO 1: IMAGEN ORIGINAL Y ESPECTRO
# ALUMNO: AREVALO RAFAEL
# NC: 0031
# ============================================================

import matplotlib.pyplot as plt

from Funciones_Frecuencia_0031 import (
    cargar_imagen,
    obtener_espectro,
    guardar_grafica
)

# Cargar imagen
imagen = cargar_imagen()

# Obtener espectro
espectro = obtener_espectro(imagen)

# Mostrar informacion
print("EJEMPLO 1: ESPECTRO DE FRECUENCIA")
print("Imagen utilizada: Monedas")
print("Alto:", imagen.shape[0])
print("Ancho:", imagen.shape[1])

# Crear graficas
figura, ejes = plt.subplots(1, 2, figsize=(12, 6))

ejes[0].imshow(imagen, cmap="gray")
ejes[0].set_title("Imagen Original: Monedas")
ejes[0].axis("off")

ejes[1].imshow(espectro, cmap="gray")
ejes[1].set_title("Espectro de Frecuencia")
ejes[1].axis("off")

plt.tight_layout()

# Guardar resultado
guardar_grafica(
    figura,
    "01_imagen_y_espectro.png"
)

plt.show()

print("-*-*-*-* Arevalo Rafael NC:0031 -*-*-*-*-")