# Números complejos
x = 3.5
print(x)
print(type(x))
y = 4
print(y)
print(type(y))
z = 2 + 3j
print(z)
print(type(z))

# Operadores aritméticos
numero1 = 10
numero2 = 3

#Suma
suma = numero1 + numero2
print("La suma es:", suma)

#Resta
resta = numero1 - numero2
print("La resta es:", resta)

#Multiplicación
multiplicacion = numero1 * numero2
print("La multiplicación es:", multiplicacion)

#División
division = numero1 / numero2
print("La división es:", division)

#Módulo
modulo = numero1 % numero2
print("El módulo es:", modulo)

#Potenciación
potenciacion = numero1 ** numero2
print("La potenciación es:", potenciacion)

# División entera
division_entera = numero1 // numero2
print("La división entera es:", division_entera)

# estructuras de control de flujo

a = 0 
b = 5

if a > b:
    print("a es mayor que b")

if a < b and a != 0:
    print("a es menor que b y a no es cero")

if a < b and a == 0:
    print("a es menor que b y a es cero")

if a < b or a != 0:
    print("a es menor que b o a no es cero")

if not b < a:
    print("b no es menor que a")

if b >= a:
    print("b es mayor o igual que a")

# Es el mismo código más reducido
# if b > a or b == a:
#     print("b es mayor que a o b es igual a a")

if a <= b:
    print("a es menor o igual que b")

# Es el mismo código más reducido
# if a == b or a < b:
#     print("a es igual que b o a es menor que b")

#if-else

"""
Diagrama de flujo de if-else
if <condition>
sentencia
else:
sentencia
"""

edad = 21

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# if-elif-else

"""
sintaxis if-elif-else
if <condition>
sentencia
elif <condition2>
sentencia
else
sentencia
"""

edad = 12

if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes 18 años entras por poco")
else:
    print("Eres mayor de edad")

# While

"""
variable=0
while <condicion>
sentencia
variable +=1
""" 

contador = 10

while contador >= 5:
    print("El contador es:", contador)
    contador -= 2

# For

# El valor de i desde 0 hasta 4
for i in range(5):
    print("El valor de i es:", i)

# El valor de i desde 2 hasta 9
for i in range(2, 10):
    print("El valor de i2 es:", i)

# El valor de i desde 1 hasta 9 con paso 2
for i in range(1, 10, 2):
    print("El valor de i3 es:", i)

# Bucle for anindado

for i in range(3):
    for j in range(2):
        print("i es:", i, "y j es:", j)

# Bucle anindado complejo

contador = 0
while contador < 3:
    for i in range(3):
        print("El valor de i es:", i)
    contador += 1

#  Introducir texto por teclado
# nombre = input("Introduce tu nombre: ")
# print("Hola", nombre)

"""
# edad  = input("Introduce tu edad: ")
edad = int(input("Introduce tu edad: "))  # Convertimos la edad a entero
print("Tienes", edad, "años")
print(type(edad))  # Por defecto la edad es un string
"""
# Salida por pantalla

nombre = "Javi"
edad = 41

print(f"hola {nombre}, tienes {edad} años")
print("hola {}, tienes {} años".format(nombre, edad))
print("Hola a todos", "mi nombre es", sep="\n", end=".\n")