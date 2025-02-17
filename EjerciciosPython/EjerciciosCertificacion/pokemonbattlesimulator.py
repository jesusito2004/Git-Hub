"""
Crea una clase Pokemon con atributos como nombre, tipo, vida y ataque.

• Implementa un método atacar(otro_pokemon), que reste puntos de vida
según el ataque.

• Controla con excepciones si otro_pokemon ya tiene vida en 0

"""

class Pokemon:
    def __init__(self, nombre, tipo, vida, ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque


def atacar(otro_pokemon):
    if otro_pokemon.vida <= 0:
        raise ValueError("El otro pokemon ya está muerto")
    otro_pokemon.vida -= 30
    return otro_pokemon.vida
# Prueba de la clase Pokemon
if __name__ == "__main__":
    pikachu = Pokemon("Pikachu", "Electrico", 100, 20)
    charizard = Pokemon("Charizard", "Fuego", 120, 30)
    print(atacar(charizard))  # Debería imprimir 110
    print(atacar(pikachu))  # Debería imprimir 90

    try:
        atacar(charizard)  # Debería lanzar una excepción
    except ValueError as e:
        print(e)  # Debería imprimir "El otro pokemon ya está muerto"

