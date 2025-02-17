"""
Objetivo: yield, generadores
Descripción:

• Crea un generador que devuelva nombres aleatorios de personajes para un
juego de rol.

• Define una función generador_nombres() que use yield para devolver
nombres de una lista.

• Cada vez que se llame al generador, debe devolver un nombre diferente hasta
agotarlos.

"""

import random

def generador_nombres():
    nombres = [
        "Aragorn", "Legolas", "Gimli", "Frodo", "Samwise", 
        "Gandalf", "Boromir", "Galadriel", "Elrond", "Arwen"
    ]
    random.shuffle(nombres)
    for nombre in nombres:
        yield nombre

# Ejemplo de uso del generador
generador = generador_nombres()
for nombre in generador:
    print(nombre)
    