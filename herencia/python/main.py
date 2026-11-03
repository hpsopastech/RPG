from personaje import Personaje
from guerrero import Guerrero
from mago import Mago
from arquero import Arquero


g = Guerrero ("Andres", 1, 100, 15, 30, 20)
m = Mago ("Pilar", 1, 70, 20, 100) 
a = Arquero ("Carlos", 1, 80, 10, 64)

print(f"¿'g' es un Personaje?: {isinstance(g, Personaje)}")
print(f"¿'m' es un Personaje?: {isinstance(m, Personaje)}")
print(f"¿'a' es un Personaje?: {isinstance(a, Personaje)}")

print(f"g esta vivo?: {g.esta_vivo()}")
print(f"m esta vivo?: {m.esta_vivo()}")
print(f"a esta vivo?: {a.esta_vivo()}")


print(g)
print(m)
print(a)
