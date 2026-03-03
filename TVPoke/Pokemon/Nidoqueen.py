from TVPoke.BaseClasses.PokeTypes import Poison, Ground
from TVPoke.BaseClasses.Move import Move

class Golduck(Poison, Ground):
    def __init__(self):
        moves = [
            Move("Earth Power", "GROUND", 40),
            Move("Sludge wave", "POISON", 40),
            Move("Surf", "WATER", 80),
            Move("Splash", "WATER", 0)
        ]
        super().__init__("Golduck", 80, moves, "./TVPoke/Pokemon/imgs/Golduck.png")