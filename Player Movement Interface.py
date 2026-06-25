from abc import ABC, abstractmethod
import random

class Player(ABC):

    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self):
        list_pos = list(self.position)
        pos = random.choice(list_pos)
        list_pos[0]+=pos[0]
        list_pos[1]+=pos[1]
        self.position = tuple(list_pos)
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0,1),(0,-1),(1,0),(-1,0)]
    def level_up(self):
        self.moves += (1,1),(-1,-1),(1,-1),(-1,1)
