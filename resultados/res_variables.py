# 1. Crea tres variable que sea una cadena de texto 

nombre: str = "Ana"
ciudad: str = "Madrid"
profesion: str = "Ingeniera"

# 2. Crea tres variables de enteros
edad: int = 28
año_nacimiento: int = 1996
numero_favorito: int = 7

# 3. Crea tres variables de flotantes

estatura: float = 1.68
peso: float = 60.5
temperatura: float = 22.3

# 4. Crea una tupla que contenga al menos un string, un booleano, un float, un entero y una variable None

mi_tupla: tuple = ("Hola", True, 3.14, 42, None)

# 5. Crea un diccionario con diferentes claves y valores
mi_diccionario: dict = {
    "nombre": nombre,
    "edad": edad,
    "estatura": estatura,
    "ciudad": ciudad,
    "profesion": profesion
}
# 6. Muestra las claves del diccionario

print(mi_diccionario.keys())

# 7. Muestra los valores del diccionario

print(mi_diccionario.values())

# 8. Crea una lista con 4 valores
mi_lista: list = [10, 20.5, "Python", False]
# 9. Borra el último valor de la lista
mi_lista.pop()
# 10. Amplia un valor float a la lista
mi_lista.append(3.14)
# 11. Borra toda la lista
mi_lista.clear()