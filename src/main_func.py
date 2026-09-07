"""
ATDF102 - Grupo 9 - Presentación final (Semana 12)
Sistema de Vales de Alimentación - Libros Impresos S.A.

Integrantes:
- Juan Diaz Palma

Detalle de archivo:
    - Archivo de funciones principales para el sistema de vales de alimentación.
    - Se realiza importacion de estructuras de datos desde data_structure.py.
"""

# ============================================================
# IMPORTACIÓN DE MÓDULOS
# ============================================================
from data_structure import *
from text_func import *


# ============================================================
# FUNCIONES DE VALIDACIÓN Y BÚSQUEDA
# ============================================================
def existe_funcionario(rut):
    """Retorna True si el rut ingresado pertenece a un funcionario registrado."""
    for f in funcionarios:
        if f["rut"] == rut:
            return True
    return False


def existe_tipo_comida(codigo):
    """Retorna True si el código ingresado corresponde a un tipo de comida registrado."""
    for t in tipos_comida:
        if t["codigo"] == codigo:
            return True
    return False


def existe_asignacion(codigo_vale):
    """Retorna True si ya existe una asignación registrada con ese código de vale."""
    return buscar_asignacion(codigo_vale) is not None


def buscar_asignacion(codigo_vale):
    """Retorna el diccionario de la asignación con ese código de vale, o None si no existe."""
    for a in asignaciones:
        if a["codigo_vale"] == codigo_vale:
            return a
    return None


def nombre_funcionario(rut):
    """Retorna el nombre del funcionario asociado a un rut."""
    for f in funcionarios:
        if f["rut"] == rut:
            return f["nombre"]
    return "Desconocido"


def existe_consumo(codigo_vale):
    """Retorna True si ese vale ya fue consumido anteriormente."""
    for c in consumos:
        if c["codigo_vale"] == codigo_vale:
            return True
    return False


def nombre_tipo_comida(codigo):
    """Retorna el nombre del tipo de comida asociado a un código."""
    for t in tipos_comida:
        if t["codigo"] == codigo:
            return t["nombre"]
    return "Desconocido"


# ============================================================
# FUNCIONES DE REGISTRO
# ============================================================
def registrar_funcionario():
    if len(funcionarios) >= MAX_FUNCIONARIOS:
        texto_limpio(
            "No es posible registrar más funcionarios (capacidad máxima alcanzada)."
        )
        return

    rut_nuevo = leer_no_vacio("Rut: ")
    if existe_funcionario(rut_nuevo):
        texto_limpio("Error: ya existe un funcionario registrado con ese rut.")
        return

    nuevo_funcionario = {
        "rut": rut_nuevo,
        "nombre": leer_no_vacio("Nombre: "),
        "calle": leer_no_vacio("Calle: "),
        "numero": leer_entero("Número: "),
        "region": leer_no_vacio("Región: "),
        "comuna": leer_no_vacio("Comuna: "),
        "email": leer_no_vacio("Email: "),
        "telefono": leer_no_vacio("Teléfono: "),
        "cargo": leer_no_vacio("Cargo: "),
        "salario_liquido": leer_flotante("Salario líquido: "),
    }
    funcionarios.append(nuevo_funcionario)
    texto_limpio("Funcionario registrado con éxito.")


def registrar_tipo_comida():
    if len(tipos_comida) >= MAX_TIPOS_COMIDA:
        texto_limpio(
            "No es posible registrar más tipos de comida (capacidad máxima alcanzada)."
        )
        return

    codigo_nuevo = leer_entero("Código: ")
    if existe_tipo_comida(codigo_nuevo):
        texto_limpio("Error: ya existe un tipo de comida con ese código.")
        return

    nuevo_tipo = {
        "codigo": codigo_nuevo,
        "nombre": leer_no_vacio("Nombre (desayuno / almuerzo / once / otro): "),
    }
    tipos_comida.append(nuevo_tipo)
    texto_limpio("Tipo de comida registrado con éxito.")


def registrar_asignacion():
    if len(asignaciones) >= MAX_ASIGNACIONES:
        texto_limpio(
            "No es posible registrar más asignaciones (capacidad máxima alcanzada)."
        )
        return

    rut_buscado = input("Rut del empleado: ")
    if not existe_funcionario(rut_buscado):
        texto_limpio("Error: el rut de empleado ingresado no está registrado.")
        return

    codigo_tipo_buscado = leer_entero("Código del tipo de comida: ")
    if not existe_tipo_comida(codigo_tipo_buscado):
        texto_limpio("Error: el código de tipo de comida ingresado no existe.")
        return

    codigo_vale_nuevo = leer_entero("Código del vale: ")
    if existe_asignacion(codigo_vale_nuevo):
        texto_limpio("Error: ya existe una asignación con ese código de vale.")
        return

    nueva_asignacion = {
        "codigo_vale": codigo_vale_nuevo,
        "rut_empleado": rut_buscado,
        "codigo_tipo_comida": codigo_tipo_buscado,
        "monto": leer_flotante("Monto del vale: "),
        "mes_asignacion": leer_mes(),
        "anio_asignacion": leer_anio(),
    }
    asignaciones.append(nueva_asignacion)
    texto_limpio("Asignación de vale registrada con éxito.")


def registrar_consumo():
    if len(consumos) >= MAX_CONSUMOS:
        texto_limpio(
            "No es posible registrar más consumos (capacidad máxima alcanzada)."
        )
        return

    codigo_vale_buscado = leer_entero("Código del vale a consumir: ")
    asignacion = buscar_asignacion(codigo_vale_buscado)
    if asignacion is None:
        texto_limpio(
            "Error: el código de vale ingresado no corresponde a ninguna asignación."
        )
        return

    rut_buscado = input("Rut del empleado: ")
    if not existe_funcionario(rut_buscado):
        texto_limpio("Error: el rut de empleado ingresado no está registrado.")
        return

    if asignacion["rut_empleado"] != rut_buscado:
        texto_limpio("Error: el vale ingresado no fue asignado a este funcionario.")
        return

    if existe_consumo(codigo_vale_buscado):
        texto_limpio("Error: este vale ya fue consumido anteriormente.")
        return

    nuevo_consumo = {
        "codigo_vale": codigo_vale_buscado,
        "rut_empleado": rut_buscado,
        "fecha_utilizacion": input("Fecha de utilización (dd/mm/aaaa): "),
        "descripcion": input("Descripción: "),
    }
    consumos.append(nuevo_consumo)
    texto_limpio("Consumo de vale registrado con éxito.")


# ============================================================
# FUNCIONES DE CONSULTA
# ============================================================
def consultar_funcionarios():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print("\n--- Listado de Funcionarios ---")
    if len(funcionarios) == 0:
        texto_limpio("No hay funcionarios registrados.")
    for f in funcionarios:
        print(
            f"{f['rut']} - {f['nombre']} - {f['cargo']} - "
            f"Salario líquido: ${f['salario_liquido']:,.0f}"
        )


def consultar_tipos_comida():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print("\n--- Listado de Tipos de Comida ---")
    if len(tipos_comida) == 0:
        texto_limpio("No hay tipos de comida registrados.")
    for t in tipos_comida:
        print(f"{t['codigo']} - {t['nombre']}")


def consultar_asignaciones():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print("\n--- Listado de Asignaciones de Vale ---")
    if len(asignaciones) == 0:
        texto_limpio("No hay asignaciones registradas.")
    for a in asignaciones:
        print(
            f"Vale {a['codigo_vale']} - Empleado: {a['rut_empleado']} - "
            f"Tipo comida: {a['codigo_tipo_comida']} - Monto: ${a['monto']:,.0f} - "
            f"Periodo: {a['mes_asignacion']}/{a['anio_asignacion']}"
        )


def consultar_consumos():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print("\n--- Listado de Consumos de Vale ---")
    if len(consumos) == 0:
        texto_limpio("No hay consumos registrados.")
    for c in consumos:
        print(
            f"Vale {c['codigo_vale']} - Empleado: {c['rut_empleado']} - "
            f"Fecha: {c['fecha_utilizacion']} - Descripción: {c['descripcion']}"
        )


# ============================================================
# FUNCIONES DE CÁLCULO
# (acumulación mediante listas paralelas, tal como se ha visto en el curso)
# ============================================================
def calcular_monto_asignado_por_tipo():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print("\n--- Monto Asignado por Tipo de Comida ---")
    codigos = []
    nombres = []
    totales = []
    for t in tipos_comida:
        codigos.append(t["codigo"])
        nombres.append(t["nombre"])
        totales.append(0.0)

    for a in asignaciones:
        for i in range(len(codigos)):
            if codigos[i] == a["codigo_tipo_comida"]:
                totales[i] += a["monto"]

    total_global = 0.0
    for i in range(len(nombres)):
        print(f"{nombres[i]}: ${totales[i]:,.0f}")
        total_global += totales[i]
    print(f"TOTAL GLOBAL ASIGNADO: ${total_global:,.0f}")


def calcular_monto_asignado_por_empleado():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print("\n--- Monto Asignado por Empleado ---")
    ruts = []
    nombres = []
    totales = []
    for f in funcionarios:
        ruts.append(f["rut"])
        nombres.append(f["nombre"])
        totales.append(0.0)

    for a in asignaciones:
        for i in range(len(ruts)):
            if ruts[i] == a["rut_empleado"]:
                totales[i] += a["monto"]

    total_global = 0.0
    for i in range(len(nombres)):
        print(f"{nombres[i]}: ${totales[i]:,.0f}")
        total_global += totales[i]
    print(f"TOTAL GLOBAL ASIGNADO: ${total_global:,.0f}")


def calcular_monto_consumido_por_tipo():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print("\n--- Monto Consumido por Tipo de Comida ---")
    codigos = []
    nombres = []
    totales = []
    for t in tipos_comida:
        codigos.append(t["codigo"])
        nombres.append(t["nombre"])
        totales.append(0.0)

    for c in consumos:
        asignacion = buscar_asignacion(c["codigo_vale"])
        if asignacion is not None:
            for i in range(len(codigos)):
                if codigos[i] == asignacion["codigo_tipo_comida"]:
                    totales[i] += asignacion["monto"]

    total_global = 0.0
    for i in range(len(nombres)):
        print(f"{nombres[i]}: ${totales[i]:,.0f}")
        total_global += totales[i]
    print(f"TOTAL GLOBAL CONSUMIDO: ${total_global:,.0f}")


def calcular_monto_consumido_por_empleado():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print("\n--- Monto Consumido por Empleado ---")
    ruts = []
    nombres = []
    totales = []
    for f in funcionarios:
        ruts.append(f["rut"])
        nombres.append(f["nombre"])
        totales.append(0.0)

    for c in consumos:
        asignacion = buscar_asignacion(c["codigo_vale"])
        if asignacion is not None:
            for i in range(len(ruts)):
                if ruts[i] == c["rut_empleado"]:
                    totales[i] += asignacion["monto"]

    total_global = 0.0
    for i in range(len(nombres)):
        print(f"{nombres[i]}: ${totales[i]:,.0f}")
        total_global += totales[i]
    print(f"TOTAL GLOBAL CONSUMIDO: ${total_global:,.0f}")
