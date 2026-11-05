from typing import Protocol

class Combatiente(Protocol):

    def esta_vivo(self) -> bool:
        ...

    def recibir_dano(self, cantidad: int) -> None:
        ...

    def atacar(self, objetivo) -> None:
        ...
