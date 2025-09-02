#Declaración
frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

#NOTA: admiten operaciones matemáticas de conjuntos, como la unión (|), la intersección (&), la diferencia (-) y la diferencia simétrica (^).
#Operaciones
union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}


interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}


diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}


diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}

#Métodos
"""
    add(elemento): agrega un elemento al conjunto.
    remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
    discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
    clear(): elimina todos los elementos del conjunto.
"""

frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()