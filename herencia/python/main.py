from personaje import Personaje
from guerrero import Guerrero
from mago import Mago
from arquero import Arquero
from monstruo import Monstruo
from item import Item
from inventario import Inventario
from mision import Mision

g = Guerrero ("Andres", 1, 100, 15, 30, 20)
m = Mago ("Pilar", 1, 70, 20, 100) 
a = Arquero ("Carlos", 1, 80, 10, 64)
x = Monstruo ("Goblin", 50, 5)
jugador = None
patORO = Item ("PATO DE ORO", "TESORO", 1000)
mis = Mision ("Recoger medicina", "50 de oro")


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
        print(f"EL {x.nombre} ha escapado")
        break
    elif opcion == "2":
        print("Has decidido huir del combate")
        print(f"El {x.nombre} Te ha dejado ir\n ")
        print(f"El {x.nombre} tiene {x.vida}/{x.vida_maxima} de vida restante")
        break

print("El combate ha terminado\n///////////////////////\nVAS CAMINANDO POR EL BOSQUE\n////////////////////\nTE HAZ ENCONTRADO UN TESORO")
print(f"Has encontrado un {patORO.nombre}")
opcion = None
while opcion == None:
    print("Deseas recogerlo?\n1. Si\n2. No")
    opcion = input("Ingresa el numero de tu opcion: ")
    if opcion == "1":
        jugador.inventario.agregar_item(patORO)
        print("Has recogido el pato de oro\nEste es tu inventario Ahora:")
        jugador.inventario.mostrar_inventario()
        break
    elif opcion == "2":
        print("Has decidido no recoger el pato de oro")
        break

print("caminando por el bosque te encuentras con un grupo de aventureros que te piden ayuda\nPara recoger medicina para un herido")
mis.agregar_personaje(jugador)
print(f"Has aceptado la mision: {mis.nombre} y tu recompensa sera: {mis.recompensa}")
