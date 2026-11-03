from personaje import Personaje


class Arquero (Personaje):
    def __init__(self, nombre, nivel, vida_maxima, ataque, flechas):
        super().__init__(nombre, nivel, vida_maxima, ataque)
        self.flechas = flechas

    def habilidad_especial(self):
        print(f"{self.nombre} usa su habilidad especial: FLECHAS EXTRA")
        self.flechas = self.flechas + 10

    def __str__(self):
        return f"{super().__str__()} | FLECHAS: {self.flechas}"

    def atacar(self, objetivo):
        if self.flechas < 1:
            print ("No tienes flechas para atacar")
        else:
            self.flechas = self.flechas - 1
            objetivo.recibir_dano(self.ataque)
