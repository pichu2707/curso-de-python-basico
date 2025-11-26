# Control de errores
# Lista de errores de python: https://docs.python.org/es/3/library/exceptions.html
"""
Tenemos un montón de código
"""
variable1 = 4+3
print(variable1)
variable2 = "hola" + " que tal"
print(variable2)
variable3 = 10-10
print(variable3)

variable800=43/variable3

# Errores de sintaxis
El problema es que está true mal escrito
if true:
    print("Es verdadero")

# Errores lógicos
a = 10
b = 5
resultado = (a - b) * 2
#Esperamos que la salida 0
print(f"resultado: {resultado}")

# Errores de ejecución
try:
    numero = int(input("Introduce un número: "))
    if numero > 5:
        print("Es verdadero")
    else:
        print("Es falso")
except Exception as e:
    print(f"Ha habido un error {e}")

try:
    numero = int(input("Introduce un número: "))
    resultado = 10/numero
    print(resultado)
except ZeroDivisionError as e:
    print(f"No se puede dividir entre cero. El error concreto es: {e}" )
except ValueError as e:
    print(f"No se puede dividir lo que estás poniendo. El error concreto es: {e}")
except Exception as e:
    print(f"Ha habido un error general {e}")

# Excepciones personalizadas
class MiExceptcionPersonalizada(Exception):
    pass

def dividir(a , b):
    if b == 0:
        raise MiExceptcionPersonalizada("AnalAIzer, NO!!!!!. No se puede dividir entre cero")
    return a/b

try:
    resultado = dividir(10, 0)
    print(resultado)
except MiExceptcionPersonalizada as e:
    print(e)

# Excepciones con notas
try:
    raise TypeError("Error de tipo")
except Exception as e:
    e.add_note("Nota adicional")
    e.add_note("Nota adicional 2")
    print(f"Ha habido un error general {e}")
    raise

def suma(a: int, b: int) -> int:
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Ambos argumentos deben ser enteros")
        return a + b
    except Exception as e:
        print(f"Ha habido un error general {e}")
        raise
print(suma("1", 2))

