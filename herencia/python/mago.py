from personaje import Personaje


class Mago (Personaje):
    def __init__(self, nombre, nivel, vida_maxima, ataque, mana):
        super().__init__(nombre, nivel, vida_maxima, ataque)
        self.mana = mana

    def __str__(self):
        return f"{super().__str__()} | MANA: {self.mana}"

    def atacar(self, objetivo, hechizo=None):

        if hechizo:
            if self.mana > 20:
                print(f"{self.nombre} lanza hechizo {hechizo}")
                self.mana = self.mana - 20
                objetivo.recibir_dano(self.ataque * 2)
            else:
                print ("No tienes Mana para lanzar hechizo")

        else:
            if self.mana < 10:
                print ("No tienes Mana para atacar")

            else:
                self.mana = self.mana - 10
                objetivo.recibir_dano(self.ataque)
