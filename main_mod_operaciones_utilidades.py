import mod_operaciones
import mod_utilidades


resultado = mod_operaciones.sumar(5, 3)
mod_utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


nombre = mod_utilidades.obtener_nombre_usuario()
mod_utilidades.imprimir_mensaje(f"Hola, {nombre}!")