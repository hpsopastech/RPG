from personaje import Personaje


class Arquero (Personaje):
    def __init__(self, nombre, nivel, vida_maxima, ataque, flechas):
        super().__init__(nombre, nivel, vida_maxima, ataque)
        self.flechas = flechas

    def __str__(self):
        return f"{super().__str__()} | FLECHAS: {self.flechas}"
