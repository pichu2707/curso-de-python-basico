import math
import os
import random
from datetime import datetime
from math import log, sqrt

# import requests

radio = 5
area = math.pi * math.pow(radio, 2)

fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

directorio_actual = os.getcwd()

print(f"El area del círculo es: {area}")
print(f"La fecha actual es: {fecha_actual}")
print(f"El directorio actual es: {directorio_actual}")


## Ejemplo número random
numero = 16
print(f"La raiz cuadrada de {numero} es igual a: {sqrt(numero)}")


print(f"calcular el log de {log(100,10)}")
