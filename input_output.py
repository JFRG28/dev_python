#NOTAS
"""
La función input() siempre devuelve una cadena de texto. 
Si deseas trabajar con otros tipos de datos, como números enteros o flotantes, 
debes realizar una conversión explícita utilizando funciones como int() o float().
"""

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")


print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

edad = int(input("Ingresa tu edad: "))


if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#Output
nombre = "Juan"
edad = 25


print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")