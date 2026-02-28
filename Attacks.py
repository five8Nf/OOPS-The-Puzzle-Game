from random import randint

class Attack():
    def __init__(self, name, min_damage, max_damage, accuracy, effect_given = None):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.base_damage = (min_damage+max_damage)/2
        self.accuracy = accuracy
        self.effect_given = effect_given
    
    def get_name(self):
        return self.name

    def get_base_damage(self):
        return self.base_damage

    def get_damage(self):

            damage = randint(self.min_damage, self.max_damage)
        return damage
    