'''
Uso de math.factorial(): Calcula el factorial de un número ingresado.
'''
import math

def factorial(i):
    if i == 10:
        return math.factorial(i)
    else:
        return "El número ingresado no es 10"
    
numero = 10
print(factorial(numero))
print("Jesús Sánchez Rodríguez")    