from Attack_list import *

class Player():
    def __init__(self, name, is_sarcastic = False):
        self.lives = 5
        self.max_hp = 100
        self.hp = 100
        self.name = name
        self.attacks = {PUNCH, KICK}
        self.inventory = {"Journal":1}
        if is_sarcastic:
            self.attacks.add(SARCASM)

    def get_hp_percentage(self):
        return self.hp / self.max_hp * 100

    def weapon_type(self, weapon_type):
        self.weapon = weapon_type