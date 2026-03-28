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

def new_screen():
    global player
    clear_screen()
    if player.lives >= 0 and player.hp >= 1:
        hp_percent = player.get_hp_percentage()
        bar_length = 20
        filled_length = int(bar_length * hp_percent / 100)
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        print(f"""The Puzzle Game
Lives: {player.lives} {"█ "*player.lives}
{player.name} HP: {player.hp:.1f}/{player.max_hp:.1f} ({hp_percent:.1f}%) [{bar}]
inventory: {player.inventory}""")
    else:
        print("""╔══════════════════════════════════════╗
║__   __            ____  _          _ ║
║\\ \\ / /__  _   _  |  _ \\(_) ___  __| |║
║ \\ V / _ \\| | | | | | | | |/ _ \\/ _` |║
║  | | (_) | |_| | | |_| | |  __/ (_| |║
║  |_|\\___/ \\__,_| |____/|_|\\___|\\__,_|║
╚══════════════════════════════════════╝""")
        quit()

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
    new_screen()
    print("""You wake up in a dark gloomy room. 
The damp walls glisten from the light of the small opening above you.
You tried to remember what had happened but you can't remember anything but this cave. 
looking around, you see two pathways. One on the left and one on the right. """)
    return input("Do you want to go left or right? ").lower()

def pillar_puzzle():
    global player
    new_screen()
    print("""You walk right and A neyon green sign appears beside you as the door behind you slams shut. 
The sign reads: 
//===================================\\\\
||You have reached the Pillar Puzzle!||
||You need to get past the pillars!  ||
||Warning Pillars are Poisonous,     ||
||Spiky,Deadly, Unbreakable, Venemous||
||Toxic, Acid Proof and covered with ||
||Acids such as HSbF2, HBR, HF, HI,  ||
||HCIO4, H2SO4, HNO3, CISO3H, HCI,   ||
||HBr, HCN and HCF3SO3.              ||
\\\\===================================//
 You look ahead serching for the pillars but you se nothing but pich black drarkness.""")
    ans = input("Input what you want to do: ").lower()
    while not "forward" in ans:
        player.lives -= 1
        new_screen()
        print("You hit a pillar and was inpailed poisoned, and dissolved by 17 different qualities of the pillars and died. ")
        input("Enter to continue...")
        new_screen()
        print("""You walk right and A neyon green sign appears beside you as the door behind you slams shut. 
The sign reads: 
//===================================\\\\
||You have reached the Pillar Puzzle!||
||You need to get past the pillars!  ||
||Warning Pillars are Poisonous,     ||
||Spiky,Deadly, Unbreakable, Venemous||
||Toxic, Acid Proof and covered with ||
||Acids such as HSbF2, HBR, HF, HI,  ||
||HCIO4, H2SO4, HNO3, CISO3H, HCI,   ||
||HBr, HCN and HCF3SO3.              ||
\\\\===================================//
 You look ahead serching for the pillars but you se nothing but pich black drarkness.""")
        ans = input("Input what you want to do: ").lower()
    new_screen()
    print("""You walk forward and run through a set of doors. 
Suddenly, torches riging the walls of the new room and the Pillar Puzzle light up revealing a sleek black handle.
a sign on the wall reads:
//=============================\\\\
||Whosoever holds this Whammer,||
||if he be worthkey,           ||
||shall possess the power of   ||
||The Fungranium.              ||
\\\\=============================//
You find it weird that the sign wrote worthkey rather then worthy but you decided to try to hold the hammer. 
As you walk up to the pedestal, you wonder what The Fungranium are as you pull the hammer out.""")
    sleep(10)
    new_screen()
    print("""You look at the object in your hand and it looks nothing like a hammer.
Thats when you realise...
It was a Whammer. You write down in your journal.
╔═══════════════════════════════════════╗
║                Whammer                ║
║This peculiar object looks like a      ║
║shriviled mushroom and a hammer        ║
║combined.
╚═══════════════════════════════════════╝""")


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
