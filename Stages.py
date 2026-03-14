import os
from time import sleep

from player import *

WEAPONS = {"1":"sword", 
           "2":"bow", 
           "3":"staff", 
           "4":"quasirhombicosidodecahedron"}

player = None

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def health():
    global player
    hp_percent = player.get_hp_percentage()
    bar_length = 20
    filled_length = int(bar_length * hp_percent / 100)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    print(f"""Lives: {player.lives} {"█ "*player.lives}
{player.name} HP: {player.hp:.1f}/{player.max_hp:.1f} ({hp_percent:.1f}%) [{bar}]""")

def loading():
    clear_screen()
    print("The Puzzle Game")
    print("Loading world")
    sleep(1)
    clear_screen()
    print("The Puzzle Game")
    print("Loading world.")
    sleep(1)
    clear_screen()
    print("The Puzzle Game")
    print("Loading world..")
    sleep(1)
    clear_screen()
    print("The Puzzle Game")
    print("Loading world...")
    sleep(1)
    clear_screen()
    print("The Puzzle Game")
    print("Loading world..")
    sleep(1)
    clear_screen()
    print("The Puzzle Game")
    print("Loading world.")
    sleep(1)
    clear_screen()
    print("The Puzzle Game")
    print("Loading world")
    sleep(1)
    clear_screen()

def intro():
    global player
    clear_screen()
    print("""/========================================================\\
||__        __   _                            _         ||
||\\ \\      / /__| | ___ ___  _ __ ___   ___  | |_ ___   ||
|| \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\  ||
||  \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | ||
||   \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/  ||
\\========================================================/""")
    sleep(5)
    clear_screen()
    print(""">>=====================================================================<<
|| _________  ___  ___  _______                                        ||
|||\\___   ___\\\\  \\|\\  \\|\\  ___ \\                                       ||
||\\|___ \\  \\_\\ \\  \\\\\\  \\ \\   __/|                                      ||
||     \\ \\  \\ \\ \\   __  \\ \\  \\_|/__                                    ||
||      \\ \\  \\ \\ \\  \\ \\  \\ \\  \\_|\\ \\                                   ||
||       \\ \\__\\ \\ \\__\\ \\__\\ \\_______\\                                  ||
||        \\|__|  \\|__|\\|__|\\|_______|                                  ||
||                                                                     ||
||                                                                     ||
||                                                                     ||
|| ________  ___  ___  ________  ________  ___       _______           ||
|||\\   __  \\|\\  \\|\\  \\|\\_____  \\|\\_____  \\|\\  \\     |\\  ___ \\          ||
||\\ \\  \\|\\  \\ \\  \\\\\  \\\\|___/  /|\\|___/  /\\ \\  \\    \\ \\   __/|         ||
|| \\ \\   ____\\ \\  \\\\\  \   /  / /    /  / /\\ \\  \\    \\ \\  \\_|/__       ||
||  \\ \\  \\___|\\ \\  \\\\\  \ /  /_/__  /  /_/__\\ \\  \\____\\ \\  \\_|\\ \\      ||
||   \\ \\__\\    \\ \\_______\\\\________\\\\________\\ \\_______\\ \\_______\\     ||
||    \\|__|     \\|_______|\\|_______|\\|_______|\\|_______|\\|_______|     ||
||                                                                     ||
||                                                                     ||
||                                                                     ||
||                     ________  ________  _____ ______   _______      ||
||                    |\\   ____\\|\\   __  \\|\\   _ \\  _   \\|\\  ___ \\     ||
||                    \\ \\  \\___|\\ \\  \\|\\  \\ \\  \\\\\__\\ \\  \\ \\   __/|    ||
||                     \\ \\  \\  __\\ \\   __  \\ \\  \\\\|__| \\  \\ \\  \\_|/__  ||
||                      \\ \\  \\|\\  \\ \\  \\ \\  \\ \\  \\    \\ \\  \\ \\  \\_|\\ \\ ||
||                       \\ \\_______\\ \\__\\ \\__\\ \\__\\    \\ \\__\\ \\_______\\||
||                        \\|_______|\\|__|\\|__|\\|__|     \\|__|\\|_______|||
>>=====================================================================<<""")
    sleep(10)
    clear_screen()
    print("The Puzzle Game")
    name = input("Input 'a name': ")
    if name.lower() == "a name":
        name = input("Good Job! now please input a name for your character: ")
        player = Player(name, True)
    else:
        player = Player(name)
    weapon = input("Please input your weapon of choice(1.Sword, 2.Bow, 3.Staff or 4.Quasirhombicosidodecahedron):")
    while not weapon in WEAPONS.keys():
        weapon = input(f"{weapon} not a valid number. Input your choice:(1.Sword, 2.Bow, 3.Staff or 4.Quasirhombicosidodecahedron):")
    clear_screen()
    print("The Puzzle Game")
    print(f"You have chosen: {WEAPONS[weapon]}")
    sleep(5)
    loading()

def room1():
    global player
    print("The Puzzle Game")
    health()
    print("""You wake up in a dark gloomy room. 
The damp walls glisten from the light of the small opening above you.
You tried to remember what had happened but you can't remember anything but this cave. 
looking around, you see two pathways. One on the left and one on the right. """)

def right():
    global player

def pillar_puzzle():
    global player

def Whammer():
    global player

def left():
    global player

def portal():
    global player

def pit_of_doom():
    global player

def colosseum():
    global player

def dirtingheim_appearence():
    global player

def workshop():
    global player

def hallway():
    global player
