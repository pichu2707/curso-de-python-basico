# Clases en Python
"""
Las clases sirven apra modelar una entidad donde podemos combinar estado --> datos (atributos) con comportamiento --> Lógica asociada a esos datos (métodos)

Esto nos ayuda a trabajar de una forma más compacta evitando:
    Variables sueltas
    Diccioanrios sin estructura
    Fuciones desconectadas

Estas clases nos permiten agrupar todo lo que pertence a algo en un único concepto
"""

# Donde usar estas clases?:
"""
Si tenemos un patrón
"""

# Sintasis de una clase
"""
class NombreClase:
    pass
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

    def cumplir_edad(self):
        self.edad += 1


p1 = Persona("Jesús", 28)
p2 = Persona("Belén", 19)

p1.saludar()
p1.cumplir_edad()
p1.saludar()


class Vehiculo:
    def __init__(self):
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def mostrar(self):
        print(self.velocidad)


c = Vehiculo()
print("Que velocidad tiene mi coche")
c.mostrar()
print("Que velocidad tiene mi coche")
c.acelerar()
c.acelerar()
c.acelerar()
c.mostrar()
print("Que velocidad tiene mi coche: ")
c.frenar()
c.mostrar()


class Usuario:
    def __init__(self, nombre, activo=True):
        self.nombre = nombre
        self.activo = activo


u1 = Usuario("Javi")
u2 = Usuario("Cristina", False)

print(u1.activo)
print(u2.activo)


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * porcentaje / 100


p = Producto("Curso de Python", 5000)
p.aplicar_descuento(80)
print(p.precio)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} - ({self.edad} años)"


p = Persona("Miguel", 55)
print(p)

# Ejemplo Landing Page
"""
vamos a ver la tasa de conversión de una landing page con el método de clases
"""


class LandingPage:
    def __init__(self, nombre, sesiones, conversiones):
        self.nombre = nombre
        self.sesiones = sesiones
        self.conversiones = conversiones

    def tasa_conversion(self):
        if self.sesiones == 0:
            return 0
        return self.conversiones / self.sesiones * 100

    def resumen(self):
        print(f"Landing: {self.nombre}")
        print(f"Sesiones: {self.sesiones}")
        print(f"Conversiones: {self.conversiones}")
        print(f"Tasa de conversión: {self.tasa_conversion():.2f}%")


lp = LandingPage("Home", 1000, 35)
print(lp.tasa_conversion())

lp1 = LandingPage("Tienda AnalAIzer", 850, 42)
lp1.resumen()
