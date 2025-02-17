"""

Objetivo: listas por compresión.

Descripción:
• En un juego de rol, cada personaje tiene un nombre, clase y nivel.
Queremos crear una lista de personajes de forma eficiente.
• Usa listas por comprensión para generar una lista de diccionarios con
personajes aleatorios.
• Cada personaje debe tener un nombre (de una lista), una clase (Guerrero,
Mago, Arquero) y un nivel aleatorio del 1 al 10.

"""
import random

# Lista de nombres
nombres = [
    "Aragorn", "Legolas", "Gimli", "Frodo", "Samwise", 
    "Gandalf", "Boromir", "Galadriel", "Elrond", "Arwen"
]

# Lista de clases
clases = ["Guerrero", "Mago", "Arquero"]

# Generar una lista de personajes usando listas por comprensión
personajes = [
    {
        "nombre": random.choice(nombres),
        "clase": random.choice(clases),
        "nivel": random.randint(1, 10)
    }
    for _ in range(10)
]

# Imprimir la lista de personajes
for personaje in personajes:
    print(personaje)
