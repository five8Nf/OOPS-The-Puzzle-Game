from random import randint, random

class Attack():
    def __init__(self, name, phrase, min_damage, max_damage, accuracy, effect = None):
        self.name = name
        self.phrase = phrase
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.base_damage = (min_damage+max_damage)/2
        self.accuracy = accuracy
        self.effect = effect
        self.keywords = ["NUMBER"]
        self.roll = 0

    def get_damage(self):
        if type(self.accuracy) == float:
            if random() > self.accuracy:
                return 0
        else:
            self.roll = randint(0, 12)
            if self.roll < 6:
                return 0
        return randint(self.min_damage, self.max_damage)

    def change_accuracy(num):
        self.accuracy = num

    def print_phrase(self):
        phrase = ""
        for word in self.phrase:
            if not word in self.keywords:
                phrase += f"{word} "
            else:
                phrase += str(self.roll)
        return phrase