from personaje import Personaje


class Guerrero (Personaje):
    def __init__(self, nombre, nivel, vida_maxima, ataque, armadura, fuerza):
        super().__init__(nombre, nivel, vida_maxima, ataque)
        self.armadura = armadura
        self.fuerza = fuerza

    def __str__(self):
        return f"{super().__str__()} | ARMADURA: {self.armadura} | FUERZA: {self.fuerza}"

    def recibir_dano(self, cantidad):
        dano_reducido = cantidad - self.armadura

        if cantidad < self.armadura:
            dano_reducido = 0
            
        super().recibir_dano(dano_reducido)
