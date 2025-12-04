
# Variables en Python

# Variables String (cadena de caracteres)
nombre: str = "Francisco Javier"
print(nombre)

apellido: str = 'Martínez'
print(apellido)

frase: str = "Hola 'esto es entre comillas' del texto"
print(frase)

frase2: str = "Hola \"Esto con comillas doble \" continua con el texto"
print(frase2)
cadena_numero: str = "40"

#Ejemplo número como string
piso = "3"
habitacion = 4
puerta = "D"
pasillo = "izquierda"

# Las variables para concatenar tienen que tener el mismo tipo
habitatantes = str(piso)+str(habitacion)
print(habitatantes)

casa = "casa del prado"
casa = casa + " en el monte"
print(casa)
# Como vemos no marca error

ejemplo: str = 40
print(f"esto es un ejemplo {ejemplo}")

# Variable números (enteros o flotantes)
edad: int = 35
print(edad)

estatura: float = 1.75
print(estatura)

# Variables números complejos
numero_complejo: complex = 3 + 4j
print(numero_complejo)

# Variables Booleanas (True o False)
es_verdadero: bool= True
es_falso: bool = False

if edad == cadena_numero:
    print("La edad y la cadena_numero son iguales")
else:
    print("La edad y la cadena_numero no son iguales")

# Variables listas, tuplas y diccionarios
lista: list = ["casa", 2, True, "siesta"]
print(lista)
print(lista[0]) # Llamamos a la lista desde la primera posición que es la cero
print(lista[3]) # Llamamos a la lista cuando tenemos claro que posición es la tres
print(lista[:3]) # Llamamos a la lista desde la primera posición hasta la posición dos
print(lista[2:]) # Llamamos a la lista desde la posición dos hasta el final

lista.append("nuevo elemento")
print(lista)
lista.remove(True)
print(lista)
lista.pop()
print(lista)
lista.clear()
print(lista)
lista.append("otro elemento")
lista.append(3.5)
lista.append(False)
print(lista)

tupla: tuple = ("perro", "gato", "ratón", "perro")
print(tupla)
tupla.count("perro")
print(tupla.count("perro"))
print(tupla.index("perro"))
print(tupla.index("gato"))

diccionario: dict = {"nombre": "Javi", "edad": 40, "es_estudiante": False}
print(diccionario)
print(diccionario)
print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["es_estudiante"])
print(diccionario.items())
print(diccionario.keys())
print(diccionario.values())
diccionario2 = {
    "nombre": nombre,
    "edad": edad,
    "es_estudiante": es_verdadero
}
print(diccionario2)

# Variables especiales (None)
none_variable: None = None
print(none_variable)
