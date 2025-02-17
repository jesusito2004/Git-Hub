import random

"""

• Crea una clase Personaje con atributos como nombre, vida y ataque.

• Implementa métodos atacar(otro_personaje) y esquivar().

• Usa random para determinar si un ataque impacta o es esquivado.

• Maneja una excepción si intentas atacar a un personaje ya derrotado

"""

class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

def atacar(otro_personaje):
    if otro_personaje.vida <= 0:
        raise ValueError("El personaje ya está derrotado")
    impacto = random.random()
    if impacto < 0.5:
        otro_personaje.vida -= 10
    else:
        print("El ataque ha sido esquivado")
    return otro_personaje.vida

def esquivar():
    impacto = random.random()
    if impacto < 0.5:
        print("El ataque ha sido esquivado")
    else:
        print("El ataque ha impactado")
    return impacto