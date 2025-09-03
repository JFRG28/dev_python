#Lectura
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#Escritura
"""
Para escribir datos en un archivo, lo abrimos en modo de escritura ("w") utilizando la función open(). 
Si el archivo no existe, se creará automáticamente. Si el archivo ya existe, su contenido se sobrescribirá.
"""

archivo = open("datos.txt", "w")
archivo.write("Hola, Python!")
print(contenido)
archivo.close()

#with
"""
Para manejar la apertura y cierre de archivos de manera automática.
"""
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

