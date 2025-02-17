"""

Objetivo: filter()
Descripción:
• Filtra personajes que tengan un nivel superior a 5 en una lista de personajes
de un juego.
• Usa filter() para obtener solo los personajes con nivel mayor a 5.
• Muestra los personajes filtrados en pantalla.

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

# Filtrar personajes con nivel superior a 5 usando filter()
personajes_filtrados = list(filter(lambda p: p['nivel'] > 5, personajes))

# Mostrar los personajes filtrados en pantalla
for personaje in personajes_filtrados:
    print(personaje)