# Listas
frutas = ["manzana", "banana", "naranja"]
#Listas de comprensión
numeros = [1, 2, 3, 4, 5]

print("Accediendo por índice positivo:")
print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"

print("Accediendo por índice negativo:")
print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"

print("Usando métodos incorporados:")
print("**append:")
frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]

print("**insert:")
frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

print("**remove:")
frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

print("**pop:")
fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

print("**sort:")
frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]

print("**reverse:")
frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

print("Listas de comprensión")
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]