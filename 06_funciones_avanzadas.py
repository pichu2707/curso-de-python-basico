# Más ejemplos con *args
# Los argumentos que son esos atributos que metemos al final en la función
def estadisticas(*args: int) -> int:
    return {
        "media": sum(args) / len(args), # len (cuenta la cantidad de elementos que hay en una variable o argumento)
        "max": max(args), # funcion max (devuelve el valor máximo de una lista o argumento)
        "min": min(args) # funcion min (devuelve el valor mínimo de una lista o argumento)
    }

print(estadisticas(10,20,30,50,100))

# Concatenación de listas
def concatenar_listas(*args: list) -> list:
    resultado = []
    for lista in args:
        resultado.extend(lista) # extend (añade los elementos de una lista a otra)
    return resultado

print(concatenar_listas([1,2,3], ['a','hola mundo','c'], [True, False, 123.45]))

# Validar que todos los argumentos son del mismo tipo
def validar_tipo_dato(*args :any) -> list:
    if not args:
        return True
    tipo = type(args[0])
    return all(isinstance(arg, tipo) for arg in args)

print(f"Validanto función con datos del mismo tipo --> {validar_tipo_dato(1,2,3,4,5,6,7,8,9)}")
print(f"Validanto función con datos de diferente tipo --> {validar_tipo_dato(1,'2',3,4,5)}")

# Más ejemplos con *kwargs
def mostrar_info(**kwargs: any) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")

mostrar_info(nombre='Javi', edad=28, ciudad='Madrid', profesion='Desarrollador')

#Ejemplo con args y kwargs juntos
def procesar(accion, *args: any, **kwargs: any) -> None:
    print(f"Acción: {accion}")

    if args:
        print("Argumentos posicionales: ")
        for arg in args:
            print(f"- {arg}")

        if kwargs:
            print("Argumentos nombrados: ")
            for clarve, valor in kwargs.items():
                print(f"- {clarve}: {valor}")

procesar(
        "creación-usuario",
        "Javi",
        "Administrador",
        email='javilazaro@analaizer.digital',
        activo=True
        )


# Funciones lambda
suma = lambda x,y: x + y
print(f"La suma de 5 + 3 es: {suma(5,3)}")

saludo = lambda nombre: f"Hola, {nombre}!"
print(saludo("Javi"))


# Funciones lambda con args
multiplicar = lambda *args: [arg * 2 for arg in args]
print(multiplicar(1,2,3,4,5))

# Funciones lambda con kwargs
procesar = lambda **kwargs: ', '.join(f"{k}={v}" for k, v in kwargs.items())
print(procesar(nombre='Javi', edad=28, ciudad='Madrid', profesion='Desarrollador'))

# Funciones lambda para ordenar listas
personas = [
    {'nombre': 'Javi', 'edad': 28},
    {'nombre': 'Ana', 'edad': 22},
    {'nombre': 'Luis', 'edad': 35}
]
ordenadas = sorted(personas, key=lambda p: p['edad'])
print(ordenadas)

# Funciones lambda mapear, filtar, reducir

#Map
numeros = [1,2,3,4,5]
dobles = list(map(lambda n: n*2, numeros))
print(f"Números dobles: {dobles}")

#Filter
pares = list(filter(lambda n: n % 2 == 0, numeros))
print(f"Números pares: {pares}")

#Reduce
from functools import reduce

producto = reduce(lambda a, b: a * b, numeros)
print(producto)

# Funciones lambda también pueden contener otras funciones lambda
aplicar = lambda func, *args, **kwargs: func(*args, **kwargs)
resultado = aplicar(lambda x, y: x ** y, 2, 3)
print(f"2 elevado a 3 es: {resultado}")
