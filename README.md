![Curso de Python desde Cero](/images/curso-python.png)
# Curso de Python

Creación de curso que está siendo retransmitido en [Twitch](https://www.twitch.tv/javilazaro1) y [Youtube](https://www.youtube.com/@JaviLazaro) con la intención que la gente tome las nociones básicas del lenguaje de programación de Python.

> Sería genial que si te ha ayudado el curso le des una "★"

## Contenido del curso
-----------------------
1. [Variables](https://www.youtube.com/watch?v=5EG7FSaCEdc&t=377s!suscriber)
2. [Flujos](https://www.youtube.com/watch?v=I6-Lc3ikfxo)

## 1. Variables y Tipos Básicos
Archivo de referencia: `02_variable.py`

En esta parte encontrarás cómo Python gestiona los tipos de forma dinámica y cómo elegir la estructura adecuada según lo que quieras representar. Aprenderás a:

- Diferenciar entre texto, números y valores lógicos (strings, enteros, flotantes, booleanos) y cuándo usar cada uno.
- Construir y manipular colecciones: listas (cuando necesitas cambiar elementos), tuplas (cuando quieres datos inmutables) y diccionarios (para asociar claves con valores).
- Entender el significado de `None` como ausencia de valor.
- Concatenar y formatear cadenas con distintos estilos.
- Aplicar operaciones frecuentes sobre listas (`append`, `remove`, `pop`, slicing), consultar información en tuplas (`count`, `index`) y recorrer la estructura de un diccionario (`items`, `keys`, `values`).

Al terminar, tendrás clara la diferencia entre cada tipo y sabrás elegir el adecuado para futuros ejercicios.

## 2. Operadores Aritméticos
Archivo: `03_flujos.py`

Aquí descubrirás cómo combinar valores numéricos y qué resultados esperar en cada caso. Verás:

- Diferencia entre división normal (`/`) y división entera (`//`) y en qué casos usar cada una.
- Cómo obtener restos con `%` para crear lógica basada en múltiplos (ideal en bucles y validaciones).
- Uso de la potencia (`**`) para cálculos exponenciales sin librerías externas.
- Pequeñas trampas comunes: resultados flotantes, precisión y conversión si necesitas un entero.

El objetivo es que puedas leer y escribir expresiones aritméticas claras y preparar valores para decisiones posteriores.

## 3. Condicionales
Archivos: `03_flujos.py`, `resultados/res_flujos.py`

Esta sección te guía para tomar decisiones en tu programa. Aprenderás a:

- Traducir reglas del mundo real (edad, rangos, estados) a bloques `if / elif / else`.
- Combinar condiciones con `and`, `or`, `not` para expresar lógica más precisa.
- Elegir comparadores adecuados (`==`, `!=`, `>`, `<`, `>=`, `<=`) y evitar redundancias.
- Diseñar bloques legibles evitando duplicar código.

Después podrás modelar fácilmente flujos como validaciones, menús o sistemas de clasificación.

## 4. Bucles
Archivos: `03_flujos.py`, `resultados/res_flujos.py`

En esta parte aprenderás patrones de repetición y cuándo usar cada tipo:

- `while`: ideal cuando no conoces de antemano cuántas iteraciones habrá (depende de una condición que puede cambiar).
- `for` con `range()`: perfecto para recorrer rangos controlados (inicio, fin y paso) y construir secuencias.
- Bucles anidados: cómo combinarlos para recorrer estructuras multidimensionales o generar patrones.
- Construcción de figuras y contadores (como el triángulo con `'*' * i`) para entender concatenación y progresión.

Al finalizar, serás capaz de elegir el bucle correcto y evitar loops infinitos por accidente.

## 5. Entrada y Salida
Aquí verás cómo interactuar con el usuario y mostrar resultados claros. Te centrarás en:

- Leer datos con `input()` y convertirlos al tipo correcto (`int`, `float`) para operar con ellos.
- Evitar errores comunes al convertir (qué pasa si el usuario escribe texto donde esperas números).
- Formatear salidas con f-strings y `format()` para mensajes amigables.
- Personalizar `print()` usando `sep` y `end` para construir salidas multi-línea o controlar finales.

Esto te permitirá crear scripts que no sólo calculan sino que comunican resultados de forma entendible.

## 6. Ejercicios (qué practicarás)
Archivo: `resultados/res_flujos.py`

Los retos están pensados para consolidar lo anterior mediante práctica guiada:

1. Manipulación básica de números (refuerza operadores y tipos).
2. Comparación y salida condicional (aplica decisiones lógicas).
3. Construcción de contadores con `for` y `while` (elige estructura adecuada).
4. Clasificación de edades (modelar reglas en condicionales encadenados).
5. Simulación de unidades/decenas/centenas (pensamiento sobre estados y acumulación).
6. Generación de figuras con texto (trabaja bucles y concatenación).

Para ampliar: valida entradas, parametriza la altura del triángulo, añade manejo de errores con `try/except`.


## Información:
Puedes encontrar más información en mi web [javilazaro.es](https://www.javilazaro.es) o bien en [AnalAIzer.digital](https://analaizer.digital) donde tienes la academia con los compañeros y donde poder compartir avances.
