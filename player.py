from Attack_list import *

class Player():
    def __init__(self, name):
        self.lives = 5
        self.maxhp = 100
        self.hp = 100
        self.name = name
        self.attacks = {PUNCH, KICK, SARCASM}
        self.inventory = dict()