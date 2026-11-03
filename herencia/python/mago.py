from personaje import Personaje


class Mago (Personaje):
    def __init__(self, nombre, nivel, vida_maxima, ataque, mana):
        super().__init__(nombre, nivel, vida_maxima, ataque)
        self.mana = mana

    def __str__(self):
        return f"{super().__str__()} | MANA: {self.mana}"
