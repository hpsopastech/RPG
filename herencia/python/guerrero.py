from personaje import Personaje


class Guerrero (Personaje):
    def __init__(self, nombre, nivel, vida_maxima, ataque, armadura, fuerza):
        super().__init__(nombre, nivel, vida_maxima, ataque)
        self.armadura = armadura
        self.fuerza = fuerza

    def __str__(self):
        return f"{super().__str__()} | ARMADURA: {self.armadura} | FUERZA: {self.fuerza}"
