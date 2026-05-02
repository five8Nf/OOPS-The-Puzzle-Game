from random import randint

class Attack():
    def __init__(self, name, phrase, min_damage, max_damage, accuracy, effect = None):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.base_damage = (min_damage+max_damage)/2
        self.accuracy = accuracy
        self.effect = effect
        self.weapon_type = weapon_name
        self.keywords = ["NUMBER"]
    
    def get_damage(self):
        damage = randint(self.min_damage, self.max_damage)
        return damage

    def print_phrase():
        for word in self.phrase:
            if not word in self.keywords:
                print(word, end= " ")
            else:
                print(randint(1, 12))