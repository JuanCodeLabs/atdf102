"""
ATDF102 - Grupo 9 - Presentación final (Semana 12)
Sistema de Vales de Alimentación - Libros Impresos S.A.

Integrantes:
- Juan Diaz Palma

Detalle de archivo:
    - Documento de datos base para el sistema de vales de alimentación.
    - Se usan listas de diccionarios para almacenar los datos de funcionarios,
    tipos de comida, asignaciones y consumos.
"""

# ============================================================
# CONSTANTES
# ============================================================
MAX_FUNCIONARIOS = 500  # int - cantidad máxima de funcionarios que admite el sistema
MAX_TIPOS_COMIDA = 10  # int - cantidad máxima de tipos de comida
MAX_ASIGNACIONES = 6000  # int - cantidad máxima de asignaciones de vale
MAX_CONSUMOS = 6000  # int - cantidad máxima de consumos de vale


# ============================================================
# ESTRUCTURAS DE DATOS (listas de diccionarios, con datos de ejemplo)
# ============================================================
funcionarios = [
    {
        "rut": "11.111.111-1",
        "nombre": "Juan Pérez",
        "calle": "Los Aromos",
        "numero": 245,
        "region": "Metropolitana",
        "comuna": "Maipú",
        "email": "juan.perez@librosimpresos.cl",
        "telefono": "+56912345678",
        "cargo": "Operador de máquina",
        "salario_liquido": 750000.0,
    },
    {
        "rut": "22.222.222-2",
        "nombre": "María Soto",
        "calle": "Las Rosas",
        "numero": 88,
        "region": "Metropolitana",
        "comuna": "Maipú",
        "email": "maria.soto@librosimpresos.cl",
        "telefono": "+56987654321",
        "cargo": "Administrativo",
        "salario_liquido": 820000.0,
    },
]

tipos_comida = [
    {"codigo": 1, "nombre": "almuerzo"},
    {"codigo": 2, "nombre": "desayuno"},
]

asignaciones = [
    {
        "codigo_vale": 1001,
        "rut_empleado": "11.111.111-1",
        "codigo_tipo_comida": 1,
        "monto": 4500.0,
        "mes_asignacion": 7,
        "anio_asignacion": 2026,
    },
    {
        "codigo_vale": 1002,
        "rut_empleado": "22.222.222-2",
        "codigo_tipo_comida": 2,
        "monto": 3000.0,
        "mes_asignacion": 7,
        "anio_asignacion": 2026,
    },
]

consumos = [
    {
        "codigo_vale": 1001,
        "rut_empleado": "11.111.111-1",
        "fecha_utilizacion": "18/07/2026",
        "descripcion": "Almuerzo casino comedor",
    },
]
