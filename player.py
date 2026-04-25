from Attack_list import *
import os

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
    
    def remove_item(self, item):
        del self.inventory[item]

    def remove_attacks(self, attack_list):
        for attack in attack_list:
            self.attacks.remove(attack)

    def new_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
        if self.hp < 1:
            self.lives -= 1
            self.hp = self.max_hp
        if self.lives >= 0 and self.hp >= 1:
            hp_percent = self.get_hp_percentage()
            bar_length = 20
            filled_length = int(bar_length * hp_percent / 100)
            bar = "█" * filled_length + "░" * (bar_length - filled_length)
            print(f"""The Puzzle Game
    Lives: {self.lives} {"█ "*self.lives}
    {self.name} HP: {self.hp:.1f}/{self.max_hp:.1f} ({hp_percent:.1f}%) [{bar}]
    inventory: {self.inventory}""")
            print("\n============================================================================================\n")
        else:
            print("""╔══════════════════════════════════════╗
║__   __            ____  _          _ ║
║\\ \\ / /__  _   _  |  _ \\(_) ___  __| |║
║ \\ V / _ \\| | | | | | | | |/ _ \\/ _` |║
║  | | (_) | |_| | | |_| | |  __/ (_| |║
║  |_|\\___/ \\__,_| |____/|_|\\___|\\__,_|║
╚══════════════════════════════════════╝""")
            quit()
