# 1. Localiza y corrige errores (sintaxis, lógicos y de ejecución)
# 1.1 Un error de sintaxis
# 1.2 Un error lógico
# 1.3 Un posible error de ejecución

numero1 = "10"
numero2 = 5

resultado = int(numero1) + int(numero2)  # Error de ejecución: Ponemos todo en int para que podamos sumar

if True: # Error de sintaxis: Falta el :
    print("El resultado es: " + str(resultado)) # Error de ejecución: No se puede sumar int con str

print("Fin del programa")


# ""
# 2.Pida al usuario dos números por teclado.
#     2.1 Intente dividir el primero entre el segundo.
#     2.2 Controle con try/except:
#     2.3 ZeroDivisionError si el segundo número es 0.
#     2.4 ValueError si el usuario introduce algo que no se puede convertir a int.
#     2.5 Cualquier otro error general con Exception.

num1 = input("Introduce el primer número: ")
num2 = input("Introduce el segundo número: ")

try:
    resultado = int(num1) / int(num2)
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero")
except ValueError:
    print("Error: Introduce números enteros")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print(f"El resultado de la división es: {resultado}")

# 3. Crea una función pedir_entero(mensaje: str) -> int que:
#     3.1 Pida un número entero al usuario usando input().
#     3.2 Use try/except para capturar ValueError.
#     3.3 Si hay error, muestre un mensaje "Eso no es un número entero" y vuelva a pedirlo.
#     3.4 Solo devuelva cuando el usuario introduce un entero válido.

def pedir_entero(mensaje: str) -> int:
    while True:
        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("Eso no es un número entero")

print(pedir_entero("Introduce un número entero: "))
# 4. El siguiente código no da error de ejecución, pero el resultado no es el esperado (error lógico).
# Encuentra el error y corrígelo usando tu razonamiento, no el intérprete.

base = 10
altura = 5

area = (base - altura) * 2  # la ecuación es incorrecta b * h 
print(f"El área del rectángulo es: {area}")

# 5. Crea una excepción personalizada llamada EdadNoValidaError que herede de Exception.
# def comprobar_edad(edad: int) -> None:
#     """
#     Lanza EdadNoValidaError si la edad es menor de 18
#     """
#     ...
#     El programa debe:

#     5.1 Pedir una edad al usuario.
#     5.2 Convertirla a int con manejo de ValueError.
#     5.3 Llamar a comprobar_edad.
try:
    edad = int(input("Introduce tu edad: "))
    comprobar_edad(edad)
except ValueError:
    print("Error: Introduce un número entero")
except EdadNoValidaError as e:
    print(e)

def comprobar_edad(edad: int) -> None:
    """
    Lanza EdadNoValidaError si la edad es menor de 18
    """
    if edad < 18:
        # "No puedes entrar, eres menor de edad".
        raise EdadNoValidaError("No puedes entrar, eres menor de edad")


# 6. Uso de raise y re-lanzar la excepción
#     Escribe una función dividir_seguro(a, b) que:
#     6.1 Controle ZeroDivisionError.
#     6.2 Si ocurre, imprima un mensaje "Intentaste dividir entre cero".
#     6.3 Después de imprimir el mensaje, vuelva a lanzar la excepción con raise para que el error siga propagándose.
#     Haz un pequeño script que llame a dividir_seguro(10, 0) dentro de un try/except y capture el error final, mostrando:
#     "Se ha producido un error en la división (nivel superior)".

def dividir_seguro(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Intentaste dividir entre cero")
        raise

try:
    resultado = dividir_seguro(10, 0)
except ZeroDivisionError:
    print("Se ha producido un error en la división (nivel superior)")

# 7. Validación de tipos como en la función suma
# Usando de inspiración la función suma(a: int, b: int) -> int que hemos visto:

#  7.1 Crea una función multiplicar(a: int, b: int) -> int que:
#     7.1.1 Verifique que ambos argumentos son int.
#     7.1.2 Si no lo son, lance un ValueError con un mensaje claro.
#     7.1.3 Devuelva la multiplicación si todo está correcto.
#  7.2 Envuelve el cuerpo en un try/except general que:
#     7.2.1 Imprima "Ha habido un error general ..."
#     7.2.2 Vuelva a lanzar la excepción con raise.
#  Haz pruebas llamando a multiplicar(3, "4") y comprueba que se lanza el error.

def multiplicar(a: int, b: int) -> int:
    try:
        return a * b
    except Exception:
        print("Ha habido un error general")
        raise

try:
    resultado = multiplicar(3, "4")
except Exception:
    print("Se ha producido un error en la multiplicación (nivel superior)")

# 8. Notas en excepciones (add_note)
# Crea un bloque try/except que:
#     8.1 Dentro del try, lance un TypeError a propósito, con el mensaje que quieras.
#     8.2 En el except Exception as e::
#     8.2.1 Añade al menos dos notas con e.add_note("...").
#     8.2.2 Imprime el mensaje principal del error y las notas de alguna forma (por ejemplo, solo imprimiendo e y re-lanzando).
#     8.2.3 Vuelve a lanzar la excepción.

try:
    raise TypeError("Error de tipo")
except Exception as e:
    e.add_note("Nota 1")
    e.add_note("Nota 2")
    print(e)
    raise

# 9. Pequeña calculadora con manejo de errores
# Haz un mini programa de calculadora que:
#     9.1 Pida al usuario:
#     9.1.1 Un número
#     9.1.2 Un segundo número
#     9.1.3 Una operación (+, -, *, /)
#     9.2 Use try/except para controlar:
#     9.2.1 ValueError al convertir a número.
#     9.2.2 ZeroDivisionError en la división.
#     9.2.3 Cualquier otro error imprevisto.
#     9.3 Si la operación no es ninguna de las cuatro, lanza manualmente un ValueError con un mensaje tipo:
#     "Operación no soportada".

num1 = input("Introduce el primer número: ")
num2 = input("Introduce el segundo número: ")
operacion = input("Introduce la operación (+, -, *, /): ")

try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print("Error: Introduce números enteros")
    raise

try:
    if operacion == "+":
        print(num1 + num2)
    elif operacion == "-":
        print(num1 - num2)
    elif operacion == "*":
        print(num1 * num2)
    elif operacion == "/":
        print(num1 / num2)
    else:
        raise ValueError("Operación no soportada")
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero")
    raise
except ValueError:
    print("Error: Operación no soportada")
    raise

# 10. Lista de números y errores encadenados
# Escribe un programa que:
#     10.1 Pida al usuario una lista de números separados por comas, por ejemplo:
#     "1,2,3,4,5".
#     10.2 Convierta esa cadena en una lista de int.
#     10.3 Calcule la media (suma / cantidad).
#     10.4 Use try/except para controlar:
#     10.4.1 ValueError si algún elemento no es un número.
#     10.4.2 ZeroDivisionError si la lista está vacía (por ejemplo, el usuario solo da espacios o nada).
#     10.4.3 Cualquier excepción general con un mensaje "Ha habido un error inesperado: ...".
# Opcional: si hay error, vuelve a pedir los datos al usuario hasta que introduzca una lista válida.""

numeros = input("Introduce una lista de números separados por comas: ").split(",")
try:
    numeros = [int(num) for num in numeros]
except ValueError:
    print("Error: Introduce números enteros")
    raise
try:
    media = sum(numeros) / len(numeros)
except ZeroDivisionError:
    print("Error: La lista está vacía")
    raise
except Exception as e:
    print(f"Ha habido un error inesperado: {e}")
    raise
print(f"La media de los números es: {media}")
