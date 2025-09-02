#Declaración
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

#Acceso
print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"

#Métodos
print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"]) devuelve una vista de todas las claves del diccionario.
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"]) devuelve una vista de todos los valores del diccionario.
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")]) devuelve una vista de todos los pares clave-valor del diccionario.


persona.update({"profesion": "Ingeniero"}) #actualiza el diccionario con los pares clave-valor de otro diccionario.
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}