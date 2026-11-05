from abc import ABC, abstractmethod
from inventario import Inventario

class Personaje(ABC):
    def __init__(self, nombre, nivel, vida_maxima, ataque):
        self.nombre = nombre
        self.nivel = nivel
        self.ataque = ataque
        self.vida_maxima = vida_maxima
        self.vida = vida_maxima
        self.inventario = Inventario()

    def __str__(self):
        return f"PERSONAJE: {self.nombre} | NIVEL: {self.nivel} | VIDA: {self.vida}/{self.vida_maxima} | ATAQUE: {self.ataque}"

    def hacer_dano(self, cantidad):
        self.vida -= cantidad

    def esta_vivo(self):
        return self.vida > 0

    def recibir_dano(self, cantidad):
        self.vida -= cantidad

    def atacar(self, objetivo):
        objetivo.recibir_dano(self.ataque)

    @abstractmethod
    def habilidad_especial(self):
        pass


    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        elif valor > self.vida_maxima:
            self._vida = self.vida_maxima
        else:
            self._vida = valor
