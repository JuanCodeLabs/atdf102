"""
ATDF102 - Grupo 9 - Presentación final (Semana 12)
Sistema de Vales de Alimentación - Libros Impresos S.A.

Integrantes:
- Juan Diaz Palma

Entrega final: se estructura el programa en distintos módulos independientes
(data_structure.py, texto_func.py, etc.) para aumentar la modularidad y legibilidad del código.

"""

# ============================================================
# IMPORTACIÓN DE MÓDULOS
# ============================================================
import sys

from data_structure import *
from main_func import *
from text_func import *


# ============================================================
# MENÚ PRINCIPAL
# ============================================================
def menu_principal():
    while True:
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()
        print("\n===== SISTEMA DE VALES DE ALIMENTACIÓN =====")
        print("1. Registrar")
        print("2. Consultar")
        print("3. Calcular")
        print("4. Salir")
        opcion = leer_entero("Ingrese una opción: ")

        if opcion == 1:
            menu_registrar()
        elif opcion == 2:
            menu_consultar()
        elif opcion == 3:
            menu_calcular()
        elif opcion == 4:
            print("Saliendo del sistema...")
            break
        else:
            texto_limpio("Opción inválida, intente nuevamente.")


# ============================================================
# SUBMENÚS
# ============================================================
def menu_registrar():
    while True:
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()
        print("\n--- Submenú Registrar ---")
        print("1. Funcionario")
        print("2. Tipo de comida")
        print("3. Asignación de vale")
        print("4. Consumo de vale")
        print("0. Volver")
        opcion = leer_entero("Ingrese una opción: ")

        if opcion == 1:
            registrar_funcionario()
        elif opcion == 2:
            registrar_tipo_comida()
        elif opcion == 3:
            registrar_asignacion()
        elif opcion == 4:
            registrar_consumo()
        elif opcion == 0:
            break
        else:
            texto_limpio("Opción inválida, intente nuevamente.")


def menu_consultar():
    while True:
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()
        print("\n--- Submenú Consultar ---")
        print("1. Funcionarios")
        print("2. Tipos de comida")
        print("3. Asignaciones")
        print("4. Consumos")
        print("0. Volver")
        opcion = leer_entero("Ingrese una opción: ")

        if opcion == 1:
            consultar_funcionarios()
            input("\nPresione Enter para volver al submenú...")
        elif opcion == 2:
            consultar_tipos_comida()
            input("\nPresione Enter para volver al submenú...")
        elif opcion == 3:
            consultar_asignaciones()
            input("\nPresione Enter para volver al submenú...")
        elif opcion == 4:
            consultar_consumos()
            input("\nPresione Enter para volver al submenú...")
        elif opcion == 0:
            break
        else:
            texto_limpio("Opción inválida, intente nuevamente.")


def menu_calcular():
    while True:
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()
        print("\n--- Submenú Calcular ---")
        print("1. Monto asignado por tipo de comida (y global)")
        print("2. Monto asignado por empleado (y global)")
        print("3. Monto consumido por tipo de comida (y global)")
        print("4. Monto consumido por empleado (y global)")
        print("0. Volver")
        opcion = leer_entero("Ingrese una opción: ")

        if opcion == 1:
            calcular_monto_asignado_por_tipo()
            input("\nPresione Enter para volver al submenú...")
        elif opcion == 2:
            calcular_monto_asignado_por_empleado()
            input("\nPresione Enter para volver al submenú...")
        elif opcion == 3:
            calcular_monto_consumido_por_tipo()
            input("\nPresione Enter para volver al submenú...")
        elif opcion == 4:
            calcular_monto_consumido_por_empleado()
            input("\nPresione Enter para volver al submenú...")
        elif opcion == 0:
            break
        else:
            texto_limpio("Opción inválida, intente nuevamente.")


# ============================================================
# INICIO DEL PROGRAMA
# ============================================================

menu_principal()
