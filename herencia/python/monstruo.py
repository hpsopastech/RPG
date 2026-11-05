from combatiente import Combatiente

class Monstruo(Combatiente):

    def __init__(self, nombre, vida_maxima, ataque):
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.ataque = ataque
        self.vida = vida_maxima

    def recibir_dano(self, cantidad):
        self.vida -= cantidad

    def atacar(self, objetivo):
        objetivo.recibir_dano(self.ataque)

    def esta_vivo(self):
        return self.vida > 0
