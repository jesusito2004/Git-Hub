'''
Ejemplo simple de uso de filtro (filter).
'''

# Genera una lista de números aleatorios entre -10 y 10, crea un filtro 
# que seleccione los números pares positivos y muestra el resultado en pantalla. 
import random

num_aleatorios = [random.randint(-10, 10) for _ in range(20)]

pares_positivos = list(filter(lambda x: x % 2 == 0 and x > 0, num_aleatorios))


print(num_aleatorios)
print(pares_positivos)




