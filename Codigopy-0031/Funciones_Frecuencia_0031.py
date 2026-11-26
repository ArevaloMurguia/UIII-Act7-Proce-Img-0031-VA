# ============================================================
# ARCHIVO: funciones_frecuencia_0031.py
# ALUMNO: Arevalo Rafael
# NC: 0031
# IMAGEN: MONEDAS
# ============================================================

import numpy as np
import cv2
import os
from skimage import data


def cargar_imagen():
    """Carga la imagen de monedas en escala de grises."""
    return data.coins()


def obtener_espectro(imagen):
    """Calcula el espectro de frecuencia mediante FFT."""
    transformada = np.fft.fft2(imagen)
    centrada = np.fft.fftshift(transformada)
    espectro = 20 * np.log(np.abs(centrada) + 1)
    return espectro


def aplicar_filtro_frecuencia(imagen, kernel):
    """Aplica un filtro mediante el dominio de frecuencia."""

    pad = 1

    imagen_padded = np.pad(
        imagen.astype(np.float32),
        pad,
        mode="reflect"
    )

    filas, columnas = imagen_padded.shape

    kernel_padded = np.zeros(
        (filas, columnas),
        dtype=np.float32
    )

    k_filas, k_columnas = kernel.shape

    inicio_fila = (filas - k_filas) // 2
    inicio_columna = (columnas - k_columnas) // 2

    kernel_padded[
        inicio_fila:inicio_fila + k_filas,
        inicio_columna:inicio_columna + k_columnas
    ] = kernel

    kernel_shifted = np.fft.ifftshift(kernel_padded)

    fft_imagen = np.fft.fft2(imagen_padded)
    fft_kernel = np.fft.fft2(kernel_shifted)

    resultado_fft = fft_imagen * fft_kernel

    resultado = np.fft.ifft2(resultado_fft)

    resultado_real = np.real(resultado)

    return resultado_real[pad:-pad, pad:-pad]


def normalizar_visualizacion(imagen):
    """Normaliza la imagen para poder visualizarla."""

    imagen_abs = np.abs(imagen)

    normalizada = cv2.normalize(
        imagen_abs,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    return normalizada.astype(np.uint8)


def guardar_grafica(figura, nombre_archivo):
    """Guarda las imágenes en la carpeta de resultados."""

    carpeta = "Resultados-Img-0031"

    os.makedirs(carpeta, exist_ok=True)

    ruta = os.path.join(carpeta, nombre_archivo)

    figura.savefig(
        ruta,
        dpi=150,
        bbox_inches="tight"
    )

    print(f"Imagen guardada correctamente: {ruta}")

print("-*-*-*-*-* Arevalo Rafael NC:0031 -*-*-*-*-*-*")