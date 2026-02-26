from Enemigo import *
from zombie import *
from ogro import *

Zombie = zombie(10, 1)
ogro = Ogro(20, 3)

print(f"{zombie.get_tipo_enemigo()}tiene{zombie.puntos_energia} de energia y ataca con {zombie.ataque} ")
print(f"{ogro.get.tipo_de_enemigo()}tiene{ogro.puntos_energia} de energia y ataaca con {ogro.ataque} ")