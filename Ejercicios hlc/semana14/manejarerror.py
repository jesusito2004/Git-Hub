'''
Manejo de excepciones (try-except): Intenta dividir un número entre 0 y captura el error.
'''
try:
    print(5 / 0)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
    print("El programa ha sido ejecutado correctamente")
    print("Jesus Sanchez Rodriguez")    