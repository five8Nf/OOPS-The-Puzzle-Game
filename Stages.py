import os
from time import sleep
from random import randint

from player import *

WEAPONS = {"1":"Sword", 
           "2":"Bow", 
           "3":"Staff", 
           "4":"Quasirhombicosidodecahedron"}

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
||\\ \\  \\|\\  \\ \\  \\\\\\  \\\\|___/  /|\\|___/  /\\ \\  \\    \\ \\   __/|         ||
|| \\ \\   ____\\ \\  \\\\\  \\   /  / /    /  / /\\ \\  \\    \\ \\  \\_|/__       ||
||  \\ \\  \\___|\\ \\  \\\\\  \\ /  /_/__  /  /_/__\\ \\  \\____\\ \\  \\_|\\ \\      ||
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
    while len(name) > 15:
        input("Name can only be 15 characters long. ")
        clear_screen()
        name = input("Input 'a name': ")
    if name.lower() == "a name":
        name = input("Good Job! now please input a name for your character: ")
        while len(name) > 15:
            input("Name can only be 15 characters long. ")
            clear_screen()
            name = input("Please input a name for your character: ")
        player = Player(name, True)
    else:
        player = Player(name)
    weapon = input("Please input the number of your weapon of choice(1.Sword, 2.Bow, 3.Staff or 4.Quasirhombicosidodecahedron): ")
    while not weapon in WEAPONS.keys():
        weapon = input(f"{weapon} not a valid number. Input your choice:(1.Sword, 2.Bow, 3.Staff or 4.Quasirhombicosidodecahedron):")
    player.weapon_choice(WEAPONS[weapon])
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
    to = input("Do you want to go left or right? ").lower()
    while to != "left" and to != "right":
        print(f"{to} is not a valid input")
        input("Next...")
        clear_screen()
        to = input("Do you want to go left or right? ")
    if to == "left":
        left()
    elif to == "right":
        new_screen()
        print("You walk right and ", end= "")
        pillar_puzzle()

def pillar_puzzle():
    global player
    print("""A neyon green sign appears beside you as the door behind you slams shut. 
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
        print("You hit a pillar and was inpailed poisoned, and dissolved by 19 different qualities of the pillars and died. ")
        input("Enter to continue...")
        new_screen()
        print("""You walk right and A neyon green sign appears beside you as the door behind you slams shut. 
The sign reads: 
//===================================\\\\
||You have reached the Pillar Puzzle!||
||You need to get past the pillars!  ||
||[!!WARNING!!] Pillars are          ||
||Poisonous, Spiky. Deadly.          ||
||Unbreakable. Venomous              ||
||Toxic. Acid-proof. Covered with    ||
||acids including but not limited to ||
||HSbF2, HBR, HF, HI, HCIO4, H2SO4,  ||
||HNO3, CISO3H, HCI, HBr, HCN and    ||
||HCF3SO3.     Writen by XD & >:3    ||
\\\\===================================//
 You look ahead serching for the pillars but you see nothing but pich black drarkness.""")
        ans = input("Input what you want to do: ").lower()
    Whammer()

def Whammer():
    global player
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
    input("Next...")
    player.add_item("Whammer", 1, WHAMMER)
    new_screen()
    print("""You look at the object in your hand and it looks nothing like a hammer.
Thats when you realise...
It was a Whammer. You write down in your journal.
╔═══════════════════════════════════════╗
║                Whammer                ║
║This peculiar object looks like a      ║
║shriviled mushroom and a hammer        ║
║combined. It does not have any effect  ║
║on anything however i did manage to    ║
║find a weird looking mushroom I dubed  ║
║"Wushroom" that was squashed into a    ║
║disgustingly sticky goopy gelatinous   ║
║mess. I haven't tried them yet so I    ║
║write them down later. On the back of  ║
║the sign, I found text saying that this║
║"Mystical" hammer holds great power and║
║can be used to smash Neyon Pink Tiles. ║
║It also said that the Neyon Pink Tiles ║
║were in memorium to the first and last ║
║Creator of Fungranium, Neyon Pink      ║
║Fungus. I suspect that this Fungranium ║
║Is a type of Stickman like myself who  ║
║Worship Mushrooms or maybe even are    ║
║Mushrooms I don't know.                ║
╚═══════════════════════════════════════╝""")
    input("Next...")
    new_screen()
    print(f"""╔═══════════════════════════════════════╗
║               Wushroom                ║
║This disgusting gelatanous mushroom    ║
║seems to puslate with great healing    ║
║energy. In my mind I heard a voice say ║
║"Hi insert_name. Creator of Hollow here║
║I have made these weird looking fungus ║
║grow across the land cus I'm bored. I  ║
║made them heal you completely or give  ║
║give you another chance to live if you ║
║are healty. But Creator of Corruption  ║
║wants things to be ballanced so it     ║
║tastes horrendous and also removes a   ║
║finger. What should I call it? Hmm...  ║
║That's a great question Spring. Aha!   ║
║How about Wushroom. That's a very      ║
║{f"creative name {player.name} let's use":<39}║
║it. " I felt confused on who this      ║
║Creator of Hollow was and why he was   ║
║talking to a spring but nevermind      ║
║Heals: 100hp/1 live                    ║
╚═══════════════════════════════════════╝""")
    input("Next...")
    new_screen()
    print("""You look around and see a clump of wushrooms on the wall. 
After swiping them off the wall, you walk back to the first room.""")
    input("Next...")
    player.add_item("Wushroom", 5)
    new_screen()
    print(f"""A small whispering voice was heard in the distance. 
Suddenly, a gigantic spiky tendirl shoots out of the wall, narrowly missing you. 
You see dark red spines on it and it turns it's tip at you and shoots forward. 
You try to dodge it but was wrapped up in a dark red snake. 
A scratchy voice rings in your head
"Ah {player.name}, you have caused many problemsssss here.
That foolishsssss Halbert thinks that you might be a greatsssss help. 
But I think notsssss. 
However I can't let you scurry aroundssssss my dead colleague'ssssss shrine can I?
I'll just help to, move thingsssssss along assssss they say. 
Just keep still and thissssss won't hurt too much. "
The giant tendril then stabbed forward and you blacked out. """)
    input("Next...")
    new_screen()
    print("""You wake up in a dark room. 
Behind you, you see a wall of scales. 
There are dark red words floating in the sky. 
They read: "This room is the path on the left. 
You cannot go back as there is a wall of impenetrable scales. 
Nobody but someone who can walk through walls can break through. " """)
    input("Next...")
    left()


def left():
    global player
    new_screen()
    if not "Whammer" in player.inventory.keys():
        print("You go left and enter a dimly lit room. ")
    print("You see two Pathways. One is a purple portal and the other has a sign saying: ")
    print("""/==============================================\\
|| _____ _  _ ___   ___ ___ _____             ||
|||_   _| || | __| | _ \\_ _|_   _|            ||
||  | | | __ | _|  |  _/| |  | |              ||
||  |_| |_||_|___| |_|_|___|_|_|__  __   ___  ||
|| / _ \\| __| |   \\ / _ \\ / _ \\|  \\/  | (_) \\ ||
||| (_) | _|  | |) | (_) | (_) | |\\/| |  _ | |||
|| \\___/|_|   |___/ \\___/ \\___/|_|  |_| (_)| |||
||                                        /_/ ||
\\==============================================/""")
    to = input("Do you want to go into the portal or THE PIT OF DOOM :): ").lower()
    while not "portal" in to and not "pit of doom" in to:
        print("that is not a valid option")
        input("Next...")
        new_screen()
        to = input("Do you want to go into the portal or THE PIT OF DOOM :): ").lower()
    if "portal" in to:
        portal()
    elif "pit of doom" in to:
        pit_of_doom()

def portal():
    global player
    new_screen()
    if not "Whammer" in player.inventory.keys():
        print("You enter the portal and in a flash of purple appear in the right hallway. ")
        input("Next...")
        new_screen()
        pillar_puzzle()
    else:
        print("You jumped in, was instantly engulfed in a sea of scales and died. ")
        input("Next...")
        player.lives -= 1
        left()

def pit_of_doom():
    global player
    new_screen()
    if not "Whammer" in player.inventory.keys():
        print("""You jumped into THE PIT OF DOOM and your screams echo through the walls of the temple.
You died to an unknown force. """)
        input("Next...")
        player.lives -= 1
        room1()
    else:
        print("""You fall down THE PIT OF DOOM and land on a mushroom. """)
        input("Next...")
        colosseum()

def colosseum():
    global player
    new_screen()
    print("""You look up and see large pillars in front of you. 
They form a loop ringing around you. 
You walk towards them and notice that they are made of dirt. 
An erie neyon pink glow appears in the distance. 
You walk towards it and climb up a small hill and see that the structure you were in was a colosseum.
Glancing at the pink glow, you see a grid of neyon pink tiles in front of you. """)
    input("Next...")
    new_screen()
    print("The top of the grid is labled 1, 2, 3 and the bottom A, B, C. ")
    number = randint(1, 3)
    if number == 1:
        ans = "A"
    elif number == 2:
        ans = "B"
    else:
        ans = "C"
    ans += str(randint(1, 3))
    accepted = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    selected = input("Input a square to hit e.g. A1, B2, C3: ").upper()
    while not selected in accepted:
        selected = input("Input a square to hit e.g. A1, B2, C3: ").upper()
    accepted.remove(selected)
    while selected != ans:
        if randint(1, 3) != 1:
            print("You got some Stone Berrys.")
            if not "Stone Berry" in player.inventory.keys():
                print(f"""╔═══════════════════════════════════════╗
║            Stone Berry                ║
║These peculiar berrys look exactly like║
║stone. They feel like stone. They      ║
║taste... *Insert puking noises* like   ║
║stone. I don't know why I tried it but ║
║I just accidentaly kicked a boulder 100║
║times my size into rubble so it seems  ║
║to make me stronger. But now my foot   ║
║hurts and my body is disgusted.        ║
║                                       ║
║                                       ║
║Son of a fish! I just stubbed my toe on║
║a small rock. Needless to say, I am not║
║strong whatsoever. I know I should     ║
║be Whammering the other tiles but oh my║
║leg hurts!                             ║
║                                       ║
║                                       ║
║                                       ║
║Strength +5                            ║
╚═══════════════════════════════════════╝""")
            player.add_item("Stone Berry", randint(1, 2))
        else:
            print("You got some Wushrooms. ")
            player.add_item("Wushroom", randint(1, 5))
        input("Next...")
        new_screen()
        selected = input("Input a square to hit e.g. A1, B2, C3: ").upper()
        while not selected in accepted:
            selected = input("Input a square to hit e.g. A1, B2, C3: ").upper()
        accepted.remove(selected)
    print(f"You got a {player.small_weapon}")
    player.add_item(player.small_weapon, 1, SMALL[player.small_weapon])
    input("next...")
    dirtingheim_appearence()
    
def dirtingheim_appearence():
    global player
    new_screen()
    print("Suddenly, the floor beneath you burst open and you slide down in to the colosseum. ")
    input("Next...")
    new_screen()
    print("""A pair of large arms start to grow. 
Dirt around you start flying up towards the arms, forming a dirtstorm. 
You squint your eyes to protect them from the flying debris.
But suddenly it stops. """)
    input("Next...")
    new_screen()
    print(""" ____  _      _   _             _          _           
|  _ \\(_)_ __| |_(_)_ __   __ _| |__   ___(_)_ __ ___  
| | | | | '__| __| | '_ \\ / _` | '_ \\ / _ \\ | '_ ` _ \\ 
| |_| | | |  | |_| | | | | (_| | | | |  __/ | | | | | |
|____/|_|_|   \\__|_|_| |_|\\__, |_| |_|\\___|_|_| |_| |_|
| |__   __ _ ___    __ ___|___/ _____ | | _____ _ __   
| '_ \\ / _` / __|  / _` \\ \\ /\\ / / _ \\| |/ / _ \\ '_ \\  
| | | | (_| \\__ \\ | (_| |\\ V  V / (_) |   <  __/ | | | 
|_| |_|\\__,_|___/  \\__,_| \\_/\\_/ \\___/|_|\\_\\___|_| |_| """)
    input("Next...")
    

def workshop():
    global player

def hallway():
    global player
