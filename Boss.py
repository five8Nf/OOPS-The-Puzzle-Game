from random import choice

class Boss():
    def __init__(self, name, hp, attacks, player):
        self.name = name
        self.max_health = hp
        self.health = hp
        self.player = player
        self.attacks = attacks

    def round_top(self):
        self.player.new_screen()
        hp_percent = self.health / self.max_health * 100
        bar_length = 40
        filled_length = int(bar_length * hp_percent / 100)
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        print(f"""{self.name} HP: {self.health:.1f}/{self.max_health:.1f} ({hp_percent:.1f}%) [{bar}]
    \n============================================================================================\n""")


# need to change
    def battle(self):
        turn = 0
        ex_damage = 0
        while True:
            self.round_top()
            if self.health < 1:
                print(f"{self.name} has been defeated.")
                input("Next...")
                break
            else:
                if turn % 2 == 0:
                    num = "1"
                    while num == "1":
                        print("""1. Inventory
2. Attack.""")
                        num = input("input the number of your choice: ")
                        while num != "1" and num != "2":
                            num = input("input the number of your choice: ")
                        if num == "1":
                            if "Wushroom" in self.player.inventory.keys() and self.player.inventory["Wushroom"] > 0:
                                print("Wushroom")
                            if "Stone Berry" in self.player.inventory.keys() and self.player.inventory["Stone Berry"] > 0:
                                print("Stone Berry")
                            chosen = input("input what you want to use: ")
                            if chosen.lower() ==  "wushroom" and self.player.inventory["Wushroom"] > 0:
                                self.player.inventory["Wushroom"] -= 1
                                if self.player.hp < self.player.max_hp:
                                    self.player.hp = 100
                                else:
                                    self.player.lives += 1
                            elif chosen.lower() ==  "stone berry" and self.player.inventory["Stone Berry"] > 0:
                                self.player.inventory["Stone Berry"] -= 1
                                ex_damage +=1
                        self.round_top()
                    self.round_top()
                    count = 1
                    all_attacks = []
                    for attack in self.player.attacks:
                        print(f"{count}. {attack.name}; Damage: {attack.base_damage}; Accuracy: {attack.accuracy}")
                        all_attacks.append(attack)
                        count += 1
                    while True:
                        try:
                            attack = int(input("Input your attack number: "))
                        except ValueError:
                            print("That is not a number.")
                            continue
                        if attack <= len(all_attacks):
                            break
                        else:
                            print("That is not a valid number.")
                    self.health -= all_attacks[attack - 1].get_damage() + ex_damage
                    self.round_top()
                    print(f"{self.player.name} {all_attacks[attack - 1].print_phrase()} {self.name}")
                    input("Next...")
                    ex_damage = 0
                else:
                    chosen = choice(list(self.attacks))
                    self.player.hp -= chosen.get_damage()
                    if self.player.hp < 1:
                        self.round_top()
                        print(f"{self.name} {chosen.print_phrase()} {self.player.name}")
                        input("Next...")
                        self.round_top()
                        print("You Failed")
                        input("Next...")
                        self.health = self.max_health
                        turn = 0
                        ex_damage = 0
                    else:
                        self.round_top()
                        print(f"{self.name} {chosen.print_phrase()}{self.player.name}")
                        input("Next...")
            turn += 1 