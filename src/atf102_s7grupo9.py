"""
ATDF102 - Grupo 9 - Avance N°3 (Semana 7)
Sistema de Vales de Alimentación - Libros Impresos S.A.

Integrantes:
- Juan Diaz Palma

Nivel intermedio: representación del diagrama de flujo / pseudocódigo
utilizando SENTENCIAS DE CONTROL (if / elif / while / for) y
ESTRUCTURAS DE DATOS (listas de diccionarios) en Python.

(Aún no se implementan funciones ni clases).
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


# ============================================================
# MENÚ PRINCIPAL (ciclo repetitivo con estructuras de control)
# ============================================================
opcion = ""  # str -> se valida y se convierte a int

while True:
    print("\n===== SISTEMA DE VALES DE ALIMENTACIÓN =====")
    print("1. Registrar")
    print("2. Consultar")
    print("3. Calcular")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")
    while not opcion.isdigit():
        opcion = input("Ingrese una opción: ")
    opcion = int(opcion)

    # --------------------------------------------------------
    # OPCIÓN 1: REGISTRAR
    # --------------------------------------------------------
    if opcion == 1:
        opcion_registrar = ""

        while True:
            print("\n--- Submenú Registrar ---")
            print("1. Funcionario")
            print("2. Tipo de comida")
            print("3. Asignación de vale")
            print("4. Consumo de vale")
            print("0. Volver")

            opcion_registrar = input("Ingrese una opción: ")
            while not opcion_registrar.isdigit():
                opcion_registrar = input("Ingrese una opción: ")
            opcion_registrar = int(opcion_registrar)

            if opcion_registrar == 1:
                if len(funcionarios) < MAX_FUNCIONARIOS:
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
                else:
                    print("No es posible registrar más funcionarios (capacidad máxima alcanzada).")

            elif opcion_registrar == 2:
                if len(tipos_comida) < MAX_TIPOS_COMIDA:
                    nuevo_tipo = {
                        "codigo": int(input("Código: ")),
                        "nombre": input("Nombre (desayuno / almuerzo / once / otro): "),
                    }
                    tipos_comida.append(nuevo_tipo)
                    print("Tipo de comida registrado con éxito.")
                else:
                    print("No es posible registrar más tipos de comida (capacidad máxima alcanzada).")

            elif opcion_registrar == 3:
                if len(asignaciones) < MAX_ASIGNACIONES:
                    rut_buscado = input("Rut del empleado: ")
                    existe_funcionario = False
                    for f in funcionarios:
                        if f["rut"] == rut_buscado:
                            existe_funcionario = True

                    if existe_funcionario:
                        codigo_tipo_buscado = int(input("Código del tipo de comida: "))
                        existe_tipo = False
                        for t in tipos_comida:
                            if t["codigo"] == codigo_tipo_buscado:
                                existe_tipo = True

                        if existe_tipo:
                            nueva_asignacion = {
                                "codigo_vale": int(input("Código del vale: ")),
                                "rut_empleado": rut_buscado,
                                "codigo_tipo_comida": codigo_tipo_buscado,
                                "monto": float(input("Monto del vale: ")),
                                "mes_asignacion": int(input("Mes de asignación: ")),
                                "anio_asignacion": int(input("Año de asignación: ")),
                            }
                            asignaciones.append(nueva_asignacion)
                            print("Asignación de vale registrada con éxito.")
                        else:
                            print("Error: el código de tipo de comida ingresado no existe.")
                    else:
                        print("Error: el rut de empleado ingresado no está registrado.")
                else:
                    print("No es posible registrar más asignaciones (capacidad máxima alcanzada).")

            elif opcion_registrar == 4:
                if len(consumos) < MAX_CONSUMOS:
                    codigo_vale_buscado = int(input("Código del vale a consumir: "))
                    existe_asignacion = False
                    for a in asignaciones:
                        if a["codigo_vale"] == codigo_vale_buscado:
                            existe_asignacion = True

                    if existe_asignacion:
                        rut_buscado = input("Rut del empleado: ")
                        existe_funcionario = False
                        for f in funcionarios:
                            if f["rut"] == rut_buscado:
                                existe_funcionario = True

                        if existe_funcionario:
                            nuevo_consumo = {
                                "codigo_vale": codigo_vale_buscado,
                                "rut_empleado": rut_buscado,
                                "fecha_utilizacion": input("Fecha de utilización (dd/mm/aaaa): "),
                                "descripcion": input("Descripción: "),
                            }
                            consumos.append(nuevo_consumo)
                            print("Consumo de vale registrado con éxito.")
                        else:
                            print("Error: el rut de empleado ingresado no está registrado.")
                    else:
                        print("Error: el código de vale ingresado no corresponde a ninguna asignación.")
                else:
                    print("No es posible registrar más consumos (capacidad máxima alcanzada).")

            elif opcion_registrar == 0:
                break

            else:
                print("Opción inválida, intente nuevamente.")

    # --------------------------------------------------------
    # OPCIÓN 2: CONSULTAR
    # --------------------------------------------------------
    elif opcion == 2:
        opcion_consultar = ""

        while True:
            print("\n--- Submenú Consultar ---")
            print("1. Funcionarios")
            print("2. Tipos de comida")
            print("3. Asignaciones")
            print("4. Consumos")
            print("0. Volver")

            opcion_consultar = input("Ingrese una opción: ")
            while not opcion_consultar.isdigit():
                opcion_consultar = input("Ingrese una opción: ")
            opcion_consultar = int(opcion_consultar)

            if opcion_consultar == 1:
                print("\n--- Listado de Funcionarios ---")
                if len(funcionarios) == 0:
                    print("No hay funcionarios registrados.")
                for f in funcionarios:
                    print(f"{f['rut']} - {f['nombre']} - {f['cargo']} - "
                          f"Salario líquido: ${f['salario_liquido']:,.0f}")

            elif opcion_consultar == 2:
                print("\n--- Listado de Tipos de Comida ---")
                if len(tipos_comida) == 0:
                    print("No hay tipos de comida registrados.")
                for t in tipos_comida:
                    print(f"{t['codigo']} - {t['nombre']}")

            elif opcion_consultar == 3:
                print("\n--- Listado de Asignaciones de Vale ---")
                if len(asignaciones) == 0:
                    print("No hay asignaciones registradas.")
                for a in asignaciones:
                    print(f"Vale {a['codigo_vale']} - Empleado: {a['rut_empleado']} - "
                          f"Tipo comida: {a['codigo_tipo_comida']} - Monto: ${a['monto']:,.0f} - "
                          f"Periodo: {a['mes_asignacion']}/{a['anio_asignacion']}")

            elif opcion_consultar == 4:
                print("\n--- Listado de Consumos de Vale ---")
                if len(consumos) == 0:
                    print("No hay consumos registrados.")
                for c in consumos:
                    print(f"Vale {c['codigo_vale']} - Empleado: {c['rut_empleado']} - "
                          f"Fecha: {c['fecha_utilizacion']} - Descripción: {c['descripcion']}")

            elif opcion_consultar == 0:
                break

            else:
                print("Opción inválida, intente nuevamente.")

    # --------------------------------------------------------
    # OPCIÓN 3: CALCULAR
    # --------------------------------------------------------
    elif opcion == 3:
        opcion_calcular = ""

        while True:
            print("\n--- Submenú Calcular ---")
            print("1. Monto asignado por tipo de comida (y global)")
            print("2. Monto asignado por empleado (y global)")
            print("3. Monto consumido por tipo de comida (y global)")
            print("4. Monto consumido por empleado (y global)")
            print("0. Volver")

            opcion_calcular = input("Ingrese una opción: ")
            while not opcion_calcular.isdigit():
                opcion_calcular = input("Ingrese una opción: ")
            opcion_calcular = int(opcion_calcular)

            if opcion_calcular == 1:
                print("\n--- Monto Asignado por Tipo de Comida ---")
                totales = {}
                for t in tipos_comida:
                    totales[t["nombre"]] = 0.0
                for a in asignaciones:
                    for t in tipos_comida:
                        if t["codigo"] == a["codigo_tipo_comida"]:
                            totales[t["nombre"]] += a["monto"]
                total_global = 0.0
                for nombre_tipo, monto_total in totales.items():
                    print(f"{nombre_tipo}: ${monto_total:,.0f}")
                    total_global += monto_total
                print(f"TOTAL GLOBAL ASIGNADO: ${total_global:,.0f}")

            elif opcion_calcular == 2:
                print("\n--- Monto Asignado por Empleado ---")
                totales = {}
                for f in funcionarios:
                    totales[f["nombre"]] = 0.0
                for a in asignaciones:
                    for f in funcionarios:
                        if f["rut"] == a["rut_empleado"]:
                            totales[f["nombre"]] += a["monto"]
                total_global = 0.0
                for nombre_emp, monto_total in totales.items():
                    print(f"{nombre_emp}: ${monto_total:,.0f}")
                    total_global += monto_total
                print(f"TOTAL GLOBAL ASIGNADO: ${total_global:,.0f}")

            elif opcion_calcular == 3:
                print("\n--- Monto Consumido por Tipo de Comida ---")
                totales = {}
                for t in tipos_comida:
                    totales[t["nombre"]] = 0.0
                for c in consumos:
                    for a in asignaciones:
                        if a["codigo_vale"] == c["codigo_vale"]:
                            for t in tipos_comida:
                                if t["codigo"] == a["codigo_tipo_comida"]:
                                    totales[t["nombre"]] += a["monto"]
                total_global = 0.0
                for nombre_tipo, monto_total in totales.items():
                    print(f"{nombre_tipo}: ${monto_total:,.0f}")
                    total_global += monto_total
                print(f"TOTAL GLOBAL CONSUMIDO: ${total_global:,.0f}")

            elif opcion_calcular == 4:
                print("\n--- Monto Consumido por Empleado ---")
                totales = {}
                for f in funcionarios:
                    totales[f["nombre"]] = 0.0
                for c in consumos:
                    for f in funcionarios:
                        if f["rut"] == c["rut_empleado"]:
                            for a in asignaciones:
                                if a["codigo_vale"] == c["codigo_vale"]:
                                    totales[f["nombre"]] += a["monto"]
                total_global = 0.0
                for nombre_emp, monto_total in totales.items():
                    print(f"{nombre_emp}: ${monto_total:,.0f}")
                    total_global += monto_total
                print(f"TOTAL GLOBAL CONSUMIDO: ${total_global:,.0f}")

            elif opcion_calcular == 0:
                break

            else:
                print("Opción inválida, intente nuevamente.")

    # --------------------------------------------------------
    # OPCIÓN 4: SALIR
    # --------------------------------------------------------
    elif opcion == 4:
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida, intente nuevamente.")