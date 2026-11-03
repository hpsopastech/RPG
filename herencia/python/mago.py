from personaje import Personaje


class Mago (Personaje):
    def __init__(self, nombre, nivel, vida_maxima, ataque, mana):
        super().__init__(nombre, nivel, vida_maxima, ataque)
        self.mana = mana

    def __str__(self):
        return f"{super().__str__()} | MANA: {self.mana}"

    def atacar(self, objetivo):
        if self.mana < 10:
            print ("No tienes Mana para atacar")
        else:
            self.mana = self.mana - 10
            objetivo.recibir_dano(self.ataque)
