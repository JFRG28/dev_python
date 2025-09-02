frutas = ["manzana", "banana", "naranja"]
contador = 0

print("Ciclo for:")
for fruta in frutas:
    print(fruta)

"""
print("Ciclo while:")
while contador < 6:
    print(contador)
    contador += 1
"""
print("Ciclo while con break:")
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break

print("Ciclo for + continue:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print("Ciclo for + pass (no hace nada):")
for i in range(5):
    pass