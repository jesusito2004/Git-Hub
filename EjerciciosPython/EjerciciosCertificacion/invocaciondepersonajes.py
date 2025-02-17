"""

Objetivo: Simular un sistema de invocación de personajes estilo Genshin Impact.

Descripción:

• Crea una clase PersonajeGacha con atributos como nombre, rareza y elemento.

• Implementa un método invocar() que devuelve un personaje aleatorio con
diferentes probabilidades según su rareza (ej. 5% para 5 , 15% para 4 y ⭐ ⭐
80% para 3⭐).

• Usa random para la probabilidad de invocación.

• Incluye un atributo privado llamado id_secreto (que será un código de 5
caracteres: dos letras mayúsculas seguidas de 3 dígitos).

"""

import random
import string

class PersonajeGacha:
    def __init__(self, nombre, rareza, elemento):
        self.nombre = nombre
        self.rareza = rareza
        self.elemento = elemento
        self.__id_secreto = self.__generar_id_secreto()

    def __generar_id_secreto(self):
        letras = ''.join(random.choices(string.ascii_uppercase, k=2))
        numeros = ''.join(random.choices(string.digits, k=3))
        return letras + numeros

    def __str__(self):
        return f"{self.nombre} (Rareza: {self.rareza}⭐, Elemento: {self.elemento})"

    @property
    def id_secreto(self):
        return self.__id_secreto

class Gacha:
    def __init__(self):
        self.personajes = [
            PersonajeGacha("Diluc", 5, "Pyro"),
            PersonajeGacha("Jean", 5, "Anemo"),
            PersonajeGacha("Fischl", 4, "Electro"),
            PersonajeGacha("Barbara", 4, "Hydro"),
            PersonajeGacha("Kaeya", 3, "Cryo"),
            PersonajeGacha("Lisa", 3, "Electro")
        ]

    def invocar(self):
        probabilidad = random.random()
        if probabilidad < 0.05:
            rareza = 5
        elif probabilidad < 0.20:
            rareza = 4
        else:
            rareza = 3

        personajes_filtrados = [p for p in self.personajes if p.rareza == rareza]
        personaje_invocado = random.choice(personajes_filtrados)
        return personaje_invocado

# Ejemplo de uso
gacha = Gacha()
personaje = gacha.invocar()
print(f"¡Has invocado a {personaje} con ID secreto {personaje.id_secreto}!")

        