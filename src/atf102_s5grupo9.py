"""
ATDF102 - Grupo 9
Sistema de Vales de Alimentación - Libros Impresos S.A.

Semana 5: representación del diagrama de flujo / pseudocódigo del
Avance N°1 utilizando Variables, Constantes y Tipos de Datos en Python.
"""
# (Aún no se implementan funciones ni ciclos de menú repetitivos;
# esa lógica se desarrollará en los siguientes avances del proyecto)
# en base a lo solicitado por la rubrica entregada por el docente.

MAX_FUNCIONARIOS = 500  # int   - cantidad máxima de funcionarios que admite el sistema
MAX_TIPOS_COMIDA = 10  # int   - cantidad máxima de tipos de comida
MAX_ASIGNACIONES = 6000  # int   - cantidad máxima de asignaciones de vale
MAX_CONSUMOS = 6000  # int   - cantidad máxima de consumos de vale

# Variables y tipos de datos - Funcionario:
rut = "11.111.111-1"  # str   - identificador único del funcionario
nombre = "Juan Pérez"  # str   - nombre completo del funcionario
calle = "Los Aromos"  # str   - calle de residencia
numero = 245  # int   - número de la vivienda
region = "Metropolitana"  # str   - región de residencia
comuna = "Maipú"  # str   - comuna de residencia
email = "juan.perez@librosimpresos.cl"  # str - correo electrónico de contacto
telefono = "+56912345678"  # str   - teléfono de contacto
cargo = "Operador de máquina"  # str - cargo que desempeña en la empresa
salario_liquido = 750000.0  # float - salario

# Variables y tipos de datos - Tipo de comida:
codigo_tipo_comida = 0  # int - identificador del tipo de comida
nombre_tipo_comida = (
    "almuerzo"  # str - nombre del tipo (desayuno, almuerzo, once, otro)
)

# Variables y tipos de datos - Asignación de vale:
codigo_vale = 1001  # int   - identificador único del vale asignado
rut_empleado = ""  # str   - rut del funcionario beneficiario del vale
monto = 4500.0  # float - valor monetario del vale
mes_asignacion = 7  # int   - mes en que se asigna el vale (1 a 12)
anio_asignacion = 2026  # int   - año en que se asigna el vale

# Variables y tipos de datos - Consumo de vale:
fecha_utilizacion = "18/07/2026"  # str - fecha en que se utilizó el vale
descripcion = "Almuerzo"  # str - detalle del consumo (producto o servicio adquirido)

# Listas para almacenar los datos:
funcionarios = [(rut, nombre, cargo, salario_liquido)]  # list
tipos_comida = [(codigo_tipo_comida, nombre_tipo_comida)]  # list
asignaciones = [(codigo_vale, rut_empleado, codigo_tipo_comida, monto)]  # list
consumos = [(codigo_vale, rut_empleado, fecha_utilizacion, descripcion)]  # list

# Contadores:
cant_funcionarios = len(funcionarios)  # int - cantidad de funcionarios registrados
cant_tipos_comida = len(tipos_comida)  # int - cantidad de tipos de comida registrados
cant_asignaciones = len(asignaciones)  # int - cantidad de asignaciones registradas
cant_consumos = len(consumos)  # int - cantidad de consumos registrados

# Variable de control del menú:
opcion = 0  # int - opción elegida por el usuario en el menú

# Menú principal (solo para ver un flujo inicial de la aplicación):
print("===== SISTEMA DE VALES DE ALIMENTACIÓN =====")
print("1. Registrar")
print("2. Consultar")
print("3. Calcular")
print("4. Salir")

# Validación de la opción ingresada por el usuario:
opcion = input("Ingrese una opción: ")
while not opcion.isdigit():  # Confirmar que la opción ingresada es un número
    opcion = input("Ingrese una opción: ")
opcion = int(opcion)

# Ejecución de la opción seleccionada por el usuario:
"""
Se registra la opción elegida por el usuario y se ejecuta la lógica correspondiente.
Actualmente, solo se implementa el directorio de opciones.
Sin funciones, sin clases, sin uso de datos.
"""
if opcion == 1:
    print("\n--- Submenú Registrar ---")
    print("1. Funcionario")
    print("2. Tipo de comida")
    print("3. Asignación de vale")
    print("4. Consumo de vale")
    print("0. Volver")

elif opcion == 2:
    print("\n--- Submenú Consultar ---")
    print("1. Funcionarios")
    print("2. Tipos de comida")
    print("3. Asignaciones")
    print("4. Consumos")
    print("0. Volver")

elif opcion == 3:
    print("\n--- Submenú Calcular ---")
    print("1. Monto asignado por tipo de comida (y global)")
    print("2. Monto asignado por empleado (y global)")
    print("3. Monto consumido por tipo de comida (y global)")
    print("4. Monto consumido por empleado (y global)")
    print("0. Volver")

elif opcion == 4:
    print("Saliendo del sistema...")
