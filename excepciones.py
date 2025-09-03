"""
El bloque try contiene el código que puede generar una excepción. 
Si ocurre una excepción dentro del bloque try, el flujo de ejecución 
se transfiere al bloque except correspondiente.
El bloque finally es opcional y se ejecuta siempre, 
independientemente de si ocurrió una excepción o no. 
Se utiliza comúnmente para realizar tareas de limpieza o liberación de recursos.
"""
try:
    # Código que puede generar una excepción
    resultado = 10 / 1.23  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")

try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción

#Excepciones personalizadas
def funcion():
    # Código que puede generar una excepción personalizada
    if condicion:
        raise Exception("Descripción del error") #Se hereda de la clase predefinida Exception


try:
    funcion()
except Exception as e:  #Se hereda de la clase predefinida Exception
    print(f"Error: {str(e)}")