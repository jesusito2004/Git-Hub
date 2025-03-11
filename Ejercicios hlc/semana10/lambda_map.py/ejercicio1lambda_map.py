
''' Función map() y lambda. '''


# Enteros de 0 a 4
lista_numerica = [x for x in range(5)]

'''
Con map() y lambda crea una nueva lista de potencias de 2 
elevado a los exponentes sacados de lista_numerica = [0,1,2,3,4].
'''
lista_cuadrados = list(map(lambda x: 2**x, lista_numerica))

print(lista_cuadrados)  # Esto imprimirá [1, 2, 4, 8, 16]

'''
Con lambda elevamos al cuadrado cada elemento de lista_cuadrados = [0,2,4,8,16].
A partir de los valores calculados, con map() obtenemos un generador  
para ser usado en el bucle for. 
'''

lista_cuadrados_al_cuadrado = map(lambda x: x**2, lista_cuadrados)


for valor in lista_cuadrados_al_cuadrado:
    print(valor)  # Esto imprimirá 1, 4, 16, 64, 256


print("Jesús Sánchez Rodríguez")
