# Sistema de Vales de Alimentación — Grupo 9

## Información general

|                 |                                        |
| --------------- | -------------------------------------- |
| **Asignatura**  | ATDF102                                |
| **Ramo**        | Fundamentos de Programación            |
| **Institución** | Universidad Andrés Bello — UNAB Online |
| **Grupo**       | N°9                                    |

---

## Estructura de carpetas

```
- chats
- docs
- src
  README.md
  diccionario-datos.md
```

## Problema a resolver

### Pregunta o desafío inicial

> ¿Cómo podemos diseñar un sistema funcional y eficiente que permita agregar funcionarios para la generación de vales alimenticios utilizando herramientas de programación y algoritmia?

### Planificación del proyecto

Desarrollo de un software que permita agregar funcionarios para la generación de vales alimenticios.

### Contexto y desarrollo del proyecto

La empresa editorial **"Libros Impresos S.A."** cuenta actualmente con una planta de 500 funcionarios, entre administrativos, operadores de máquinas, dobladores, maestros, etc., que trabajan en turnos para cubrir la operación de la empresa las 24 horas del día.

Debido a que la empresa se encuentra alejada de centros comerciales y restaurantes, ha adoptado la modalidad de entregar servicio de desayuno, almuerzo y once como un beneficio para sus funcionarios. Para esto genera vales de colación, personalizados por cada turno, que son entregados a los funcionarios y que pueden ser cobrados en los dos casinos (cafetería y comedor) implementados en la empresa. Estos vales son valorizados (monto del vale) y personalizados (rut del beneficiario). Para los servicios de alimentación se ha contratado una empresa externa que, además de los servicios indicados (desayuno, almuerzo, once), ofrece otras alternativas de alimentación que pueden ser cubiertas por el valor del vale.

En relación a lo anterior, la empresa requiere el desarrollo de un software que permita **agregar funcionarios**, para lo cual debe almacenar la siguiente información: rut, nombre, calle, número, región, comuna, email, teléfono, cargo, salario líquido.

También debe permitir **agregar tipos de comida**: código, nombre (desayuno, almuerzo, once, otro (ejemplo: merienda)).

Además, se debe almacenar la información de la **asignación de vales**: rut del empleado, código del vale, código del tipo de comida, monto, mes de asignación, año de asignación.

Finalmente, se deben registrar los **vales consumidos** por los empleados, tales como: código del vale, rut del empleado, fecha de utilización, descripción.

### El programa debe permitir consultar:

- Empleados registrados
- Tipos de comida registradas
- Asignación de vales de alimentación
- Consumo de vales de alimentación

### El programa también debe permitir visualizar:

- Asignación de vales
- El monto total de dinero asignado de los vales (por tipo de comida y global)
- El monto total de dinero asignado de los vales (por empleado y global)
- El monto total de dinero consumido de los vales (por tipo de comida y global)
- El monto total de dinero consumido de los vales (por empleado y global)

---

## Detalle de la primera entrega (Avance N°1 - Semana 3)

Esta entrega corresponde a la **primera parte del proyecto** y consiste en desarrollar, un prototipo de solución algorítmica para el problema asignado por el docente. Concretamente, se debe entregar:

1. **Diagrama de flujo de datos (DFD) o pseudocódigo** — representando los procesos, relaciones de datos y lógica de la solución.
2. **Diccionario de datos** — describiendo cada una de las variables, constantes y/o estructuras de datos utilizadas, indicando tipo de dato y función.

---

## Estado actual del proyecto

- [x] Diagrama de Flujo de Datos (DFD) del sistema
- [x] Pseudocódigo completo (proceso principal + 12 subprocesos/funciones)
- [x] Diccionario de datos conceptual (independiente del lenguaje de programación)

> **Nota:** el diccionario de datos de esta entrega se elaboró en términos neutros (Alfanumérico, Numérico entero, Numérico decimal, Fecha), de modo que pueda adaptarse fácilmente al lenguaje o motor de base de datos que el grupo defina en etapas posteriores del proyecto.

```

```
