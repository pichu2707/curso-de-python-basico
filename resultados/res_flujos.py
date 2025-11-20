# 1. Crea dos a través de teclado int 
num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
# 2. Suma los números 
suma = num1 + num2
# 3. Resta los números
resta = num1 - num2
# 4. Multiplica los dos números
multiplicacion = num1 * num2
# 5. Haz una comparativa de los números y que nos diga cual es mayor y cual es menor
if num1 > num2:
    print(f"El número {num1} es mayor que {num2}")
elif num1 < num2:
    print(f"El número {num2} es mayor que {num1}")
# 6. Haz que nos cuente un bucle con for y con while desde el número que marcaste primero hasta el segundo de uno en uno
print("Contador con for:")
for i in range(num1, num2 + 1):
    print(i)
print("Contador con while:")
contador = num1 
while contador <= num2:
    print(contador)
    contador += 1
# 7. Divide el número y di que resto tendría
division = num1 // num2
resto = num1 % num2
print(f"La división de {num1} entre {num2} es {division} con un resto de {resto}")
# 8. Escribe una edad y que diga cuanto le falta para ser mayor de edad (18 años) adulto (hasta los 50) maduro (en adelante)
edad = int(input("Introduce tu edad: "))
if edad < 18:
    print(f"Te faltan {18 - edad} años para ser mayor de edad.")
elif 18 <= edad < 50:
    print(f"Te faltan {50 - edad} años para ser adulto.")
else:
    print("Eres maduro.")
# 9. Haz un contador de unidades que por cada decena se sume y de ahí hasta llegar a 100 y cuente la centena
unidades = 0
decenas = 0
centenas = 0
for i in range(1, 101):
    unidades += 1
    for j in range(10):
        for k in range(10):
            pass
    if unidades == 10:
        unidades = 0
        decenas += 1
        if decenas == 10:
            decenas = 0
            centenas += 1
    print(f"Número: {i}, Centenas: {centenas}, Decenas: {decenas}, Unidades: {unidades}")
# 10. Dibuja un triángulo con for usando * como puntero altura del triángulo al menos tienes que ser 5
altura = 5
for i in range(1, altura + 1):
    print('*' * i) 