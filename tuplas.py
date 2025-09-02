# No se pueden agregar, eliminar o cambiar elementos
punto = (3, 4)
mi_tupla = (1, 2, 3, 2, 4, 2)

print("Accediendo por índice: ")
print(punto[0])  # Imprime 3
print(punto[1])  # Imprime 4

print("Usando métodos incorporados:")
print("**count:")
print (mi_tupla.count(2))   # Salida: 3
print("**index:")
print (mi_tupla.index(2, 2, 4))   #Salida: 3 ya que se indica el valor,pos_ini,pos_fin
print("**len:")
print (len(mi_tupla))   # Salida: 6