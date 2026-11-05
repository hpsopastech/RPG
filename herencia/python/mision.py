class Mision:
    def __init__(self, nombre, recompensa):
        self.nombre = nombre
        self.recompensa = recompensa
        self.personajes = []

    def agregar_personaje(self, personaje):
        self.personajes.append(personaje)
