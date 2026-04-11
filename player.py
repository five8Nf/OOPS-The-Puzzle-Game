from Attack_list import *

SMALLS = {"Sword" : "Handle", 
          "Bow" : "Thin Stick", 
          "Staff" : "Short Stick", 
          "Quasirhombicosidodecahedron" : "Dodecahedron"}

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

    def weapon_choice(self, weapon_name):
        self.weapon_type = weapon_name
        self.small_weapon = SMALLS[weapon_name]

    def add_item(self, item, quantity, new_attacks = None):
        if item in self.inventory.keys():
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        if new_attacks != None:
            self.attacks = self.attacks | new_attacks