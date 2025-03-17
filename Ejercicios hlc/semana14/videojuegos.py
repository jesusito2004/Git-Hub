'''
Buscar un elemento en una lista: Crea una lista de videojuegos y permite al usuario buscar uno.
'''
# Crea una lista de videojuegos
videojuegos = ["Minecraft", "Fortnite", "Call of Duty", "PlayerUnknown"]
print(videojuegos)
# Pide al usuario que ingrese el nombre de un videojuego
nombre_videojuego = input("Ingrese el nombre de un videojuego: ")
# Busca el videojuego en la lista
if nombre_videojuego in videojuegos:
    print(f"El videojuego '{nombre_videojuego}' se encuentra en la lista.")
else:
    print(f"El videojuego '{nombre_videojuego}' no se encuentra en la lista.")
    


