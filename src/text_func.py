"""
ATDF102 - Grupo 9 - Presentación final (Semana 12)
Sistema de Vales de Alimentación - Libros Impresos S.A.

Integrantes:
- Juan Diaz Palma

Detalle de archivo:
    - Definición de validadores de texto para
    leer datos de entrada específicos por el usuario.
"""

# ============================================================
# IMPORTACIÓN DE MÓDULOS
# ============================================================
import sys
import time

# ============================================================
# VALIDADORES DE TEXTO
# ============================================================


def leer_entero(mensaje):
    """Solicita un valor por teclado hasta que corresponda a un número entero válido."""
    valor = input(mensaje)
    while not valor.isdigit():
        print("Error: el valor debe ser un número entero.")
        valor = input(mensaje)
    return int(valor)


# Se agrega función para leer un número decimal. Funciona al igual que leer_entero.
def leer_flotante(mensaje):
    """Solicita un valor por teclado hasta que corresponda a un número decimal válido."""
    valor = input(mensaje)
    while True:
        try:
            return float(valor)
        except ValueError:
            print("Error: el valor debe ser un número decimal.")
            valor = input(mensaje)


# Se agrega función para evitar campos vacios.
def leer_no_vacio(mensaje):
    """Solicita un texto por teclado hasta que no esté vacío (ni compuesto solo por espacios)."""
    texto = input(mensaje).strip()
    while texto == "":
        print("Error: este campo no puede quedar vacío.")
        texto = input(mensaje).strip()
    return texto


# Se agrega función para leer un mes válido.
def leer_mes():
    """Solicita un mes válido (entre 1 y 12)."""
    mes = leer_entero("Mes de asignación (1-12): ")
    while mes < 1 or mes > 12:
        print("Error: el mes debe estar entre 1 y 12.")
        mes = leer_entero("Mes de asignación (1-12): ")
    return mes


# Se agrega función para leer un año válido. Solo para evitar números negativos.
def leer_anio():
    """Solicita un año válido (mayor o igual a 2000)."""
    anio = leer_entero("Año de asignación: ")
    while anio < 2000:
        print("Error: ingrese un año válido (2000 en adelante).")
        anio = leer_entero("Año de asignación: ")
    return anio


def texto_limpio(mensaje, espera=0.8):
    """Limpia la pantalla de la consola, muestra un mensaje y espera
    brevemente antes de continuar. Reemplaza el bloque repetido de
    sys.stdout.write + flush + print + time.sleep usado en los mensajes
    de error y éxito del sistema."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print(mensaje)
    time.sleep(espera)
