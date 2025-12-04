# 1. Función que reciba un nombre y devuelva un saludo
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Javi"))

# 2. Función que calcule el área de un triángulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

print(calcular_area_triangulo(3, 4))

# 3. Función que determine si un número es par o impar
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(4))

# 4. Función que reciba una lista y devuelva su longitud
def longitud_lista(lista):
    return len(lista)

print(longitud_lista([1, 2, 3, 4, 5]))

# 5. Función que cuente cuántas vocales hay en un texto
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

print(contar_vocales("Hola, mundo!"))

# 6. Función que reciba un número n y devuelva una lista con los n primeros números de Fibonacci
def fibonacci(n):
    lista = []
    a, b = 0, 1
    for i in range(n):
        lista.append(a)
        a, b = b, a + b
    return lista

print(fibonacci(10))

# 7. Función que reciba una lista y devuelva otra lista sin elementos repetidos (sin usar set)
def eliminar_repetidos(lista):
    lista_sin_repetidos = []
    for elemento in lista:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)
    return lista_sin_repetidos

print(eliminar_repetidos([1, 2, 2, 3, 4, 4, 5]))

# 8. Función que acepte un número variable de argumentos y devuelva su suma
def sumar(*args):
    return sum(args)

print(sumar(1, 2, 3, 4, 5))

# 9. Función que reciba un diccionario y devuelva otro diccionario con las claves ordenadas alfabéticamente
def ordenar_claves(diccionario):
    return {key: diccionario[key] for key in sorted(diccionario)}

print(ordenar_claves({"c": 3, "a": 1, "b": 2}))

# 10. Función que actúe como un pequeño validador de contraseñas
def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if not any(c.isupper() for c in contraseña):
        return False
    if not any(c.islower() for c in contraseña):
        return False
    if not any(c.isdigit() for c in contraseña):
        return False
    return True

print(validar_contraseña("contraseña123"))
