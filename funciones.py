#NOTAS: no existen funciones sobrecargadas. Siempre se toma la última que esté definida.
#al poner dentro del paréntesis de los parámetros de la función el * significa que recibe N cantidad de parámetros (args)

#Declaración
#Sin parámetro
def saludo():
    print("¡Hola, mundo!")

#Con parámetro
def saludo(nombre):
    print(f"¡Hola, {nombre}!")

#Con retorno
def suma(a, b):
    return a + b

#Uso
#Sin parámetro
#saludo()  # Imprime "¡Hola, mundo!"

#Con parámetro
saludo("Juan")  # Imprime "¡Hola, Juan!"
saludo("María")  # Imprime "¡Hola, María!"

#Con retorno
resultado = suma(3, 4)
print(resultado)  # Imprime 7

#Funciones anónimas (Lambda)
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25

#Alcance de variables (local vs global)
def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función

variable_global = 20

def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar

funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
#print(variable_local)  # Genera un error, la variable no está definida en este alcance.

#Usando args
def calcular_media(*numeros):
    suma=sum(numeros)
    cantidad=len(numeros)
    media=suma/cantidad
    return media

print("Media: ",calcular_media(10,20,30))

#Documentar funciones
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura

print("Área rectángulo: ",area_rectangulo(28,89))