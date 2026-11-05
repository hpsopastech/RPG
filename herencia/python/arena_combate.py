from combatiente import Combatiente

class ArenaCombate:

    def __init__(self, combatiente1: Combatiente, combatiente2: Combatiente):
        self.combatiente1 = combatiente1
        self.combatiente2 = combatiente2

    def iniciar_combate(self):
        print("///////////////////////\nCOMBATE\n///////////////////////")
        print("ESTE COMBATE SERA A MUERTE")

        while self.combatiente1.esta_vivo()==True and self.combatiente2.esta_vivo()==True:
            print(f"\nCombatiente 1 esta vivo: {self.combatiente1.esta_vivo()}")
            print(f"Combatiente 2 esta vivo: {self.combatiente2.esta_vivo()}")

            print("\n///////////////////////\nTURNO DE ATAQUE\n///////////////////////")
            
            self.combatiente1.atacar(self.combatiente2)
            if self.combatiente2.esta_vivo()==False:
                print("\nEl combatiente 2 ha sido derrotado")
                break

            self.combatiente2.atacar(self.combatiente1)
            if self.combatiente1.esta_vivo()==False:
                print("\nEl combatiente 1 ha sido derrotado")
                break

        if self.combatiente1.esta_vivo()==True:
            print(f"\nEl ganador es {self.combatiente1.nombre}")
        else:
            print(f"\nEl ganador es {self.combatiente2.nombre}")
