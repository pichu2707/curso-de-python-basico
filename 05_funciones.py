# Cómo definir una función
# def nombre_de_la_funcion(parametro1, parametro2):
#     return resultado
def suma(a: int, b: int) -> int:
    resultado = a + b
    return resultado

print(f"La solución de la suma es: {suma(2, 3)}")


def nombre_edad(a: str, b: int) -> str:
    """
    Función para mostrar el nombre y la edad de una persona
    args:
        a (str): nombre de la persona
        b (int): edad de la persona
    return:
        str: nombre y edad de la persona
    """
    return f"{a} tiene {b} años"

print(nombre_edad("Juan", 30))

# Argumentos y parámetros de las funciones en python
def nombre_edad(a = "javi", b = 41) -> str:
    return f"{a} tiene {b} años"

print(nombre_edad("Juan", 30))
print(nombre_edad())

def mayor_edad(edad: int) -> int:
    if edad > 18:
        print("Eres mayor de edad")
    elif edad == 18:
        print("Entras por los pelos")
    else:
        print("Eres menor de edad")
mayor_edad(10)
mayor_edad(18)
mayor_edad(20)

# Retornando funciones
def crear_multiplicador(factor: int) -> int:
    def multiplicar(numero: int) -> int:
        return numero * factor
    return multiplicar


duplicar=crear_multiplicador(2)
print(type(duplicar))
triplicar=crear_multiplicador(3)
print(duplicar(5))
print(triplicar(5))
# Funciones recursivas

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(0))
print(factorial(5))

# Excepciones en funciones
def dividir(a: int, b: int) -> float:
    try:
        resultado = a/b
    except ZeroDivisionError:
        return "Error: No puedes divir entre 0 cazurro"
    else:
        return resultado

print(dividir(10, 2))
print(dividir(10, 0))

# Aserciones en funciones
def calcular_raiz_cuadrada(x: int) -> float:
    assert x >= 0, "No se puede calcular la raiz cuadrada de un numero negativo"
    return x ** 0.5

print(f"La raiz cuadrada de 4 es: {calcular_raiz_cuadrada(4)}")
# print(f"La raiz cuadrada de -4 es: {calcular_raiz_cuadrada(-4)}")
# Argumentos variables
# Ejemplo más explicativo
def sumar(*args: int) -> int:
    s = 0
    for arg in args:
        s += arg
    return s

print(sumar(1, 2, 3, 4, 5))

# Ejemplo simplificado
def sumar(*args: int) -> int:
    return sum(args)

print(sumar(1, 2, 3, 4, 5))

def sumar(a: int, b: int, c: int, *args: int, **kwargs: int) -> int:
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    for arg in args:
        print("arg = ", arg)
    for key, value in kwargs.items():
        print("key = ", key, "value = ", value)

sumar(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, nombre="Juan", edad=30)

def sumar(a: int, b: int, c: int, **kwargs: dict) -> int:
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)

    for key, value in kwargs.items():
        print("key = ", key, "value = ", value)

sumar(10, 20, 30, nombre="Juan", edad=30)

