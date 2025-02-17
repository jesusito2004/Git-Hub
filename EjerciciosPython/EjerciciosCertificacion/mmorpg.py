"""
Crea una clase Item con atributos como nombre, tipo y rareza.

• Crea una clase Personaje que tenga un inventario (lista de objetos).

• Implementa un método agregar_item(item) que añada objetos al
inventario, con un máximo de 5 objetos.

• Si el inventario está lleno, lanza una excepción personalizada
InventarioLlenoError

"""

class Item:
    def __init__(self, nombre, tipo, rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza

class InventarioLlenoError(Exception):
    """Excepción personalizada para cuando el inventario está lleno"""
    pass

class Personaje:
    def __init__(self):
        self.inventario = []
        self.max_inventario = 5

    def agregar_item(self, item):
        """
        Agrega un objeto al inventario si hay espacio disponible.

        Args:
            item (Item): Objeto a agregar al inventario.

        Raises:
            InventarioLlenoError: Si el inventario está lleno.
        """
        if len(self.inventario) < self.max_inventario:
            self.inventario.append(item)
        else:
            raise InventarioLlenoError("El inventario está lleno")

# Crear un personaje
personaje = Personaje()

# Crear objetos
objeto1 = Item("Espada", "Arma", "Común")
objeto2 = Item("Escudo", "Defensa", "Rare")
objeto3 = Item("Poción", "Consumible", "Común")

# Agregar objetos al inventario
personaje.agregar_item(objeto1)
personaje.agregar_item(objeto2)
personaje.agregar_item(objeto3)

# Intentar agregar más objetos que el máximo permitido
for _ in range(3):
    try:
        personaje.agregar_item(Item("Objeto", "Tipo", "Rareza"))
    except InventarioLlenoError as e:
        print(e)

