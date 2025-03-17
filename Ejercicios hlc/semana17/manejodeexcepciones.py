'''Manejo de excepciones con finally: Intenta abrir un archivo existente y usa finally'''
try:
    archivo = open('archivo.txt', 'r')
    contenido = archivo.read()
    print(contenido)
finally:
    archivo.close()
    print('Fin del programa')

print("Jesús Sánchez Rodríguez")