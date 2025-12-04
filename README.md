![Curso de Python desde Cero](/images/curso-python.png)
# Curso de Python

Creación de curso que está siendo retransmitido en [Twitch](https://www.twitch.tv/javilazaro1) y [Youtube](https://www.youtube.com/@JaviLazaro) con la intención que la gente tome las nociones básicas del lenguaje de programación de Python.

> Sería genial que si te ha ayudado el curso le des una "★"

## Contenido del curso
-----------------------
1. [Variables](https://www.youtube.com/watch?v=5EG7FSaCEdc&t=377s!suscriber)
2. [Flujos](https://www.youtube.com/watch?v=I6-Lc3ikfxo)
3. [Control de errores](https://www.youtube.com/watch?v=I6-Lc3ikfxo)

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

## 7. Control de errores
Archivo de referencia: `04_control_errores.py` donde estamos viendo los errores que pueden ocurrir y como controlarlos.

En este directo hemos trabajado uno de los pilares fundamentales de cualquier lenguaje de programación: el control de errores. Entender cómo se producen, cómo identificarlos y cómo gestionarlos correctamente nos permite escribir código más robusto, más profesional y mucho más fácil de depurar.

Durante la sesión hemos recorrido los diferentes tipos de errores que pueden aparecer en Python, desde los más básicos hasta el uso de excepciones personalizadas y notas en excepciones. Aquí tienes un resumen de todo lo que hemos tratado:

### 1. Errores de sintaxis

Son los errores que aparecen antes de que el programa pueda ejecutarse. Suelen venir por:
* Paréntesis sin cerrar
* Palabras clave mal escritas
* Falta de dos puntos
* Indentación incorrecta

### 2. Errores lógicos
El programa se ejecuta, pero el resultado es incorrecto porque la lógica es errónea.

### 3. Errores de ejecución (Runtime Errors)
Son errores que aparecen mientras el programa está funcionando.
Aquí ya entran las excepciones: `ValueError`, `ZeroDivisionError`, etc.

### 4. Excepciones personalizadas
Creamos nuestras propias excepciones para dar mensajes más claros y adaptados al contexto.

### 5. Añadir notas a excepciones
También vimos cómo enriquecer las excepciones con notas adicionales:

### 6. Validación de tipos y buenas prácticas
Reforzamos la importancia de validar los argumentos antes de usarlos.

El objetivo ha sido que entiendas:
- Qué tipos de errores existen
- Cómo reconocerlos cuando aparecen
- Cómo capturarlos sin que tu programa deje de funcionar
- Cómo crear tus propias excepciones
- Cómo escribir funciones seguras y fiables
Ahora tienes la base para manejar errores como un verdadero desarrollador profesional y evitar horas de frustración buscando fallos.

## 8. Ejercicios (qué practicarás)
Archivo: `resultados/res_control_errores.py`

## 9. Funciones
Funciones en Python — Resumen del Temario
Este documento resume los conceptos vistos en clase sobre funciones en Python. El vídeo asociado contiene todos los ejemplos prácticos, por lo que aquí solo se incluye la explicación teórica.

### 1. ¿Qué es una función?
Una función es un bloque de código reutilizable que permite agrupar instrucciones para realizar una tarea concreta.
* Sirven para:
* Evitar repetir código
* Mejorar la organización
* Facilitar el mantenimiento
* Trabajar de forma modular

### 2. Cómo definir una función
Para crear una función se utiliza la palabra clave def, seguida del nombre de la función y sus parámetros.
Una función puede devolver un valor mediante return.

### 3. Documentación de funciones (Docstrings)
Las funciones pueden llevar documentación interna para:
* Explicar qué hace la función
* Describir los parámetros
* Indicar qué devuelve
Esto ayuda a otros desarrolladores (y a ti mismo en el futuro) a entender el propósito de la función.

### 4. Parámetros y argumentos
Las funciones pueden recibir valores llamados parámetros.
Los valores que se pasan al llamar a la función se llaman argumentos.

Python permite:
* Parámetros obligatorios
* Parámetros opcionales con valores por defecto
* Parámetros nombrados

### 5. Condicionales dentro de funciones
Dentro de una función se pueden usar estructuras de control como:
* if
* elif
* else
Para tomar decisiones en base a los datos recibidos.

### 6. Funciones que retornan funciones (Closures)
Python permite que una función devuelva otra función.
Esto se usa para:
* Crear funciones personalizadas
* Generar configuraciones internas
* Aplicar patrones de diseño como funciones fábrica

### 7. Funciones recursivas
Una función recursiva es aquella que se llama a sí misma.
Se usa para:
* Problemas que se pueden dividir en partes más pequeñas
* Cálculos matemáticos como factoriales
* Algoritmos sobre estructuras como árboles o directorios
Siempre deben incluir un caso base para evitar recursión infinita.

### 8. Manejo de excepciones en funciones
El manejo de errores se realiza mediante:
* try
* except
* else
Permite controlar situaciones como divisiones por cero, tipos incorrectos, etc., evitando que el programa se detenga.

### 9. Aserciones
Las aserciones se utilizan para verificar que una condición se cumple.
Si no se cumple, se lanza un error con un mensaje personalizado.
Son útiles para validar parámetros antes de continuar la ejecución.

### 10. Argumentos variables: *args y **kwargs
Python permite funciones con un número variable de argumentos:
***args** → recibe argumentos posicionales ilimitados
****kwargs** → recibe argumentos con nombre ilimitados
Esto permite crear funciones muy flexibles que aceptan diferentes combinaciones de valores.

## Información:
Puedes encontrar más información en mi web [javilazaro.es](https://www.javilazaro.es) o bien en [AnalAIzer.digital](https://analaizer.digital) donde tienes la academia con los compañeros y donde poder compartir avances.
