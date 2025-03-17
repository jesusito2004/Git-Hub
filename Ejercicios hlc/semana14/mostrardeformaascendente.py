'''
MÓDULO 2: Cadenas, Métodos de Listas y Cadenas, y Excepciones.
Ordenar una lista: Pide al usuario una lista de números separados por comas y muéstralos en orden ascendente.
'''
# Pide al usuario una lista de números separados por comas
numeros = input("Introduce una lista de números separados por comas: ")
# Separa los números de la cadena y los convierte a enteros
numeros = [int(x) for x in numeros.split(",")]
# Ordena la lista en orden ascendente
numeros.sort()
# Muestra la lista ordenada
print("La lista ordenada es: ", numeros)


print("Jesus Sanchez Rodriguez")    