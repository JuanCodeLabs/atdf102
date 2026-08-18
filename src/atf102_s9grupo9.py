"""
ATDF102 - Grupo 9 - Avance N°4 (Semana 9)
Sistema de Vales de Alimentación - Libros Impresos S.A.

Integrantes:
- Juan Diaz Palma

Nivel avanzado: se incorpora PROGRAMACIÓN MODULAR (funciones en Python)
sobre las mismas estructuras de datos y de control usadas en el Avance N°3
(listas de diccionarios, if / elif / while / for). No se incorporan
conocimientos fuera de lo visto en la Unidad 3 (listas, strings, funciones,
módulos).

Corrección aplicada según feedback del docente (Avance N°3):
- Al registrar un consumo, antes solo se comprobaba que el código de vale
  existiera y que el funcionario existiera, por separado. Ahora también se
  valida que ese vale haya sido asignado específicamente a ese funcionario,
  evitando que se registre el consumo de un vale de otro empleado.
"""

# ============================================================
# CONSTANTES
# ============================================================
MAX_FUNCIONARIOS = 500     # int - cantidad máxima de funcionarios que admite el sistema
MAX_TIPOS_COMIDA = 10      # int - cantidad máxima de tipos de comida
MAX_ASIGNACIONES = 6000    # int - cantidad máxima de asignaciones de vale
MAX_CONSUMOS = 6000        # int - cantidad máxima de consumos de vale


# ============================================================
# ESTRUCTURAS DE DATOS (listas de diccionarios, con datos de ejemplo)
# ============================================================
funcionarios = [
    {
        "rut": "11.111.111-1", "nombre": "Juan Pérez", "calle": "Los Aromos",
        "numero": 245, "region": "Metropolitana", "comuna": "Maipú",
        "email": "juan.perez@librosimpresos.cl", "telefono": "+56912345678",
        "cargo": "Operador de máquina", "salario_liquido": 750000.0,
    },
    {
        "rut": "22.222.222-2", "nombre": "María Soto", "calle": "Las Rosas",
        "numero": 88, "region": "Metropolitana", "comuna": "Maipú",
        "email": "maria.soto@librosimpresos.cl", "telefono": "+56987654321",
        "cargo": "Administrativo", "salario_liquido": 820000.0,
    },
]

tipos_comida = [
    {"codigo": 1, "nombre": "almuerzo"},
    {"codigo": 2, "nombre": "desayuno"},
]

asignaciones = [
    {
        "codigo_vale": 1001, "rut_empleado": "11.111.111-1", "codigo_tipo_comida": 1,
        "monto": 4500.0, "mes_asignacion": 7, "anio_asignacion": 2026,
    },
    {
        "codigo_vale": 1002, "rut_empleado": "22.222.222-2", "codigo_tipo_comida": 2,
        "monto": 3000.0, "mes_asignacion": 7, "anio_asignacion": 2026,
    },
]

consumos = [
    {
        "codigo_vale": 1001, "rut_empleado": "11.111.111-1",
        "fecha_utilizacion": "18/07/2026", "descripcion": "Almuerzo casino comedor",
    },
]
'''
Se realiza integración de definiciones de funciones en base a las necesidades
de la aplicación.
'''

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


def nombre_tipo_comida(codigo):
    """Retorna el nombre del tipo de comida asociado a un código."""
    for t in tipos_comida:
        if t["codigo"] == codigo:
            return t["nombre"]
    return "Desconocido"


def leer_entero(mensaje):
    """Solicita un valor por teclado hasta que corresponda a un número entero válido."""
    valor = input(mensaje)
    while not valor.isdigit():
        valor = input(mensaje)
    return int(valor)

# ============================================================
# FUNCIONES DE REGISTRO
# ============================================================
def registrar_funcionario():
    if len(funcionarios) >= MAX_FUNCIONARIOS:
        print("No es posible registrar más funcionarios (capacidad máxima alcanzada).")
        return

    nuevo_funcionario = {
        "rut": input("Rut: "),
        "nombre": input("Nombre: "),
        "calle": input("Calle: "),
        "numero": int(input("Número: ")),
        "region": input("Región: "),
        "comuna": input("Comuna: "),
        "email": input("Email: "),
        "telefono": input("Teléfono: "),
        "cargo": input("Cargo: "),
        "salario_liquido": float(input("Salario líquido: ")),
    }
    funcionarios.append(nuevo_funcionario)
    print("Funcionario registrado con éxito.")


def registrar_tipo_comida():
    if len(tipos_comida) >= MAX_TIPOS_COMIDA:
        print("No es posible registrar más tipos de comida (capacidad máxima alcanzada).")
        return

    nuevo_tipo = {
        "codigo": leer_entero("Código: "),
        "nombre": input("Nombre (desayuno / almuerzo / once / otro): "),
    }
    tipos_comida.append(nuevo_tipo)
    print("Tipo de comida registrado con éxito.")


def registrar_asignacion():
    if len(asignaciones) >= MAX_ASIGNACIONES:
        print("No es posible registrar más asignaciones (capacidad máxima alcanzada).")
        return

    rut_buscado = input("Rut del empleado: ")
    if not existe_funcionario(rut_buscado):
        print("Error: el rut de empleado ingresado no está registrado.")
        return

    codigo_tipo_buscado = leer_entero("Código del tipo de comida: ")
    if not existe_tipo_comida(codigo_tipo_buscado):
        print("Error: el código de tipo de comida ingresado no existe.")
        return

    nueva_asignacion = {
        "codigo_vale": leer_entero("Código del vale: "),
        "rut_empleado": rut_buscado,
        "codigo_tipo_comida": codigo_tipo_buscado,
        "monto": float(input("Monto del vale: ")),
        "mes_asignacion": leer_entero("Mes de asignación: "),
        "anio_asignacion": leer_entero("Año de asignación: "),
    }
    asignaciones.append(nueva_asignacion)
    print("Asignación de vale registrada con éxito.")


def registrar_consumo():
    """
    Registra el consumo de un vale.

    Corrección de feedback del docente: ya no basta con que el vale exista
    y con que el funcionario exista por separado; además se comprueba que
    el vale ingresado haya sido asignado justamente a ese funcionario.
    """
    if len(consumos) >= MAX_CONSUMOS:
        print("No es posible registrar más consumos (capacidad máxima alcanzada).")
        return

    codigo_vale_buscado = leer_entero("Código del vale a consumir: ")
    asignacion = buscar_asignacion(codigo_vale_buscado)
    if asignacion is None:
        print("Error: el código de vale ingresado no corresponde a ninguna asignación.")
        return

    rut_buscado = input("Rut del empleado: ")
    if not existe_funcionario(rut_buscado):
        print("Error: el rut de empleado ingresado no está registrado.")
        return

    if asignacion["rut_empleado"] != rut_buscado:
        print("Error: el vale ingresado no fue asignado a este funcionario.")
        return

    nuevo_consumo = {
        "codigo_vale": codigo_vale_buscado,
        "rut_empleado": rut_buscado,
        "fecha_utilizacion": input("Fecha de utilización (dd/mm/aaaa): "),
        "descripcion": input("Descripción: "),
    }
    consumos.append(nuevo_consumo)
    print("Consumo de vale registrado con éxito.")


# ============================================================
# FUNCIONES DE CONSULTA
# ============================================================
def consultar_funcionarios():
    print("\n--- Listado de Funcionarios ---")
    if len(funcionarios) == 0:
        print("No hay funcionarios registrados.")
    for f in funcionarios:
        print(f"{f['rut']} - {f['nombre']} - {f['cargo']} - "
              f"Salario líquido: ${f['salario_liquido']:,.0f}")


def consultar_tipos_comida():
    print("\n--- Listado de Tipos de Comida ---")
    if len(tipos_comida) == 0:
        print("No hay tipos de comida registrados.")
    for t in tipos_comida:
        print(f"{t['codigo']} - {t['nombre']}")


def consultar_asignaciones():
    print("\n--- Listado de Asignaciones de Vale ---")
    if len(asignaciones) == 0:
        print("No hay asignaciones registradas.")
    for a in asignaciones:
        print(f"Vale {a['codigo_vale']} - Empleado: {a['rut_empleado']} - "
              f"Tipo comida: {a['codigo_tipo_comida']} - Monto: ${a['monto']:,.0f} - "
              f"Periodo: {a['mes_asignacion']}/{a['anio_asignacion']}")


def consultar_consumos():
    print("\n--- Listado de Consumos de Vale ---")
    if len(consumos) == 0:
        print("No hay consumos registrados.")
    for c in consumos:
        print(f"Vale {c['codigo_vale']} - Empleado: {c['rut_empleado']} - "
              f"Fecha: {c['fecha_utilizacion']} - Descripción: {c['descripcion']}")


# ============================================================
# FUNCIONES DE CÁLCULO
# (acumulación mediante listas paralelas, tal como se ha visto en el curso)
# ============================================================
def calcular_monto_asignado_por_tipo():
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

'''
Se realiza integración de definiciones de funciones para mejorar la 
legibilidad del código y menús de funcionalidades.
'''

# ============================================================
# SUBMENÚS
# ============================================================
def menu_registrar():
    while True:
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
            print("Opción inválida, intente nuevamente.")


def menu_consultar():
    while True:
        print("\n--- Submenú Consultar ---")
        print("1. Funcionarios")
        print("2. Tipos de comida")
        print("3. Asignaciones")
        print("4. Consumos")
        print("0. Volver")
        opcion = leer_entero("Ingrese una opción: ")

        if opcion == 1:
            consultar_funcionarios()
        elif opcion == 2:
            consultar_tipos_comida()
        elif opcion == 3:
            consultar_asignaciones()
        elif opcion == 4:
            consultar_consumos()
        elif opcion == 0:
            break
        else:
            print("Opción inválida, intente nuevamente.")


def menu_calcular():
    while True:
        print("\n--- Submenú Calcular ---")
        print("1. Monto asignado por tipo de comida (y global)")
        print("2. Monto asignado por empleado (y global)")
        print("3. Monto consumido por tipo de comida (y global)")
        print("4. Monto consumido por empleado (y global)")
        print("0. Volver")
        opcion = leer_entero("Ingrese una opción: ")

        if opcion == 1:
            calcular_monto_asignado_por_tipo()
        elif opcion == 2:
            calcular_monto_asignado_por_empleado()
        elif opcion == 3:
            calcular_monto_consumido_por_tipo()
        elif opcion == 4:
            calcular_monto_consumido_por_empleado()
        elif opcion == 0:
            break
        else:
            print("Opción inválida, intente nuevamente.")


# ============================================================
# MENÚ PRINCIPAL
# ============================================================
def menu_principal():
    while True:
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
            print("Opción inválida, intente nuevamente.")


menu_principal()