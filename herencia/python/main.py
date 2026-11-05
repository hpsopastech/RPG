from personaje import Personaje
from guerrero import Guerrero
from mago import Mago
from arquero import Arquero
from monstruo import Monstruo


g = Guerrero ("Andres", 1, 100, 15, 30, 20)
m = Mago ("Pilar", 1, 70, 20, 100) 
a = Arquero ("Carlos", 1, 80, 10, 64)
x = Monstruo ("Goblin", 50, 5)
jugador = None

print(f"¿'g' es un Personaje?: {isinstance(g, Personaje)}")
print(f"¿'m' es un Personaje?: {isinstance(m, Personaje)}")
print(f"¿'a' es un Personaje?: {isinstance(a, Personaje)}")

print(f"g esta vivo?: {g.esta_vivo()}")
print(f"m esta vivo?: {m.esta_vivo()}")
print(f"a esta vivo?: {a.esta_vivo()}")


print(g)
print(m)
print(a)

g.habilidad_especial()
m.habilidad_especial()
a.habilidad_especial()



while jugador == None:
    print("Elige Quien Quieres Ser\n1. Andres el Guerrero\n2. Pilar la Maga\n3. Carlos el Arquero")
    opcion = input("Ingresa el numero de tu opcion: ")
    if opcion == "1":
        jugador = g
    elif opcion == "2":
        jugador = m
    elif opcion == "3":
        jugador = a

opcion = None
print(f"Has elegido ser {jugador.nombre}")

print("Ah llegado un monstruo a atacarte\nDECIDE QUE VAS A HACER\n1. Atacar\n2. Huir")
while opcion == None:
    opcion = input("Ingresa el numero de tu opcion: ")
    if opcion == "1":
        jugador.atacar(x)
        print(f"Has atacado al {x.nombre} y le has hecho {jugador.ataque} de daño")
        print(f"El {x.nombre} tiene {x.vida}/{x.vida_maxima} de vida restante")
    elif opcion == "2":
        print("Has decidido huir del combate")
        print(f"El {x.nombre} Te a dejado ir\n ")
        print(f"El {x.nombre} tiene {x.vida}/{x.vida_maxima} de vida restante")
