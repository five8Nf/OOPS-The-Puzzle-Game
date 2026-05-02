class Boss():
    def __init__(self, name, hp, attacks, player):
        self.name = name
        self.max_health = hp
        self.health = hp
        self.player = player

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
        while True:
            self.round_top()
            if self.health < 1:
                print(f"{self.name} has been defeated.")
                input("Next...")
                break
            else:
                if turn % 2 == 0:
                    count = 1
                    for attack in self.player.attacks:
                        print(f"{count}. {attack.name}; Damage: {attack.base_damage}; Accuracy: {attack.accuracy}")
                        count += 1
                    while True:
                        try:
                            attack = int(input("Input your attack number: "))
                        except ValueError:
                            print("That is not a number.")
                            attack = 0
                        if attack <= len(self.player.attacks):
                            break
                        else:
                            print("That is not a valid number.")
                        # list(self.player.attacks)[]
                    self.health = 0
                # else:
            turn += 1 
