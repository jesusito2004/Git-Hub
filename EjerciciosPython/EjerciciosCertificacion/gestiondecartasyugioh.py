"""
Objetivo: Crear un sistema de manejo de cartas de Yu-Gi-Oh! con OOP.

Descripción:

• Crea una clase Carta con atributos como nombre, ataque, defensa y tipo.

• Implementa una clase Jugador con un mazo de cartas.

• Crea un método invocar_carta(nombre) para colocar una carta en juego.

• Si la carta no está en el mazo, lanza una excepción personalizada CartaNoEncontradaError.

"""

class Carta:
    def __init__(self, nombre, ataque, defensa, tipo):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} (ATK: {self.ataque}, 
    DEF: {self.defensa}, Tipo: {self.tipo})"

class CartaNoEncontradaError(Exception):
    pass


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mazo = []
    def agregar_carta(self, carta):
        self.mazo.append(carta)       



def invocar_carta(self, nombre):
    for carta in self.mazo:
        if carta.nombre == nombre:
            print(f"{self.nombre} ha invicado a {carta}")
            return carta
        raise CartaNoEncontradaError(f"Carta '{nombre}' no encontrada 
        en el mazo de {self.nombre}")
    
#Ejemplos de uso

carta1 = Carta("Dragón Blanco de Ojos Azules", 3000, 2500, "Dragón")
carta2 = Carta("Mago Oscuro", 2500, 2100, "Mago")

jugador = Jugador("Yugi")
jugador.agregar_carta(carta1)
jugador.agregar_carta(carta2) 
    




    