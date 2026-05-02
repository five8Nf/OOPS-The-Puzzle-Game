import os
from time import sleep
from random import randint
from inputimeout import inputimeout, TimeoutOccurred

from Boss import *
from Attack_list import *
from Player import *

player = None

def get_player():
    return player

WEAPONS = {"1":"Sword", 
           "2":"Bow", 
           "3":"Staff", 
           "4":"Quasirhombicosidodecahedron"}

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def input_sec(text, sec, ans):
    try:
        user_input = inputimeout(prompt= text, timeout= sec).lower()
        if user_input != ans:
            return False
        else:
            return True
    except TimeoutOccurred:
        return False
        

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
    player.new_screen()
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
        player.new_screen()
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
    while (not "forward" in ans) and (not "straight" in ans):
        player.lives -= 1
        player.new_screen()
        print("You hit a pillar and was inpailed poisoned, and dissolved by 19 different qualities of the pillars and died. ")
        input("Enter to continue...")
        player.new_screen()
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
 You look ahead serching for the pillars but you see nothing but pitch black drarkness.""")
        if player.lives == 0:
            ans = input("you Feel O sliRht sensation tugging you. WhAt Ro you want to Do:")
        else:
            ans = input("Input what you want to do: ").lower()
    Whammer()

def Whammer():
    global player
    player.new_screen()
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
    player.new_screen()
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
    player.new_screen()
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
    player.new_screen()
    print("""You look around and see a clump of wushrooms on the wall. 
After swiping them off the wall, you walk back to the first room.""")
    input("Next...")
    player.add_item("Wushroom", 5)
    player.new_screen()
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
    player.new_screen()
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
    player.new_screen()
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
        player.new_screen()
        to = input("Do you want to go into the portal or THE PIT OF DOOM :): ").lower()
    if "portal" in to:
        portal()
    elif "pit of doom" in to:
        pit_of_doom()

def portal():
    global player
    player.new_screen()
    if not "Whammer" in player.inventory.keys():
        print("You enter the portal and in a flash of purple appear in the right hallway. ")
        input("Next...")
        player.new_screen()
        pillar_puzzle()
    else:
        print("You jumped in, was instantly engulfed in a sea of scales and died. ")
        input("Next...")
        player.lives -= 1
        left()

def pit_of_doom():
    global player
    player.new_screen()
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
    player.new_screen()
    print("""You look up and see large pillars in front of you. 
They form a loop ringing around you. 
You walk towards them and notice that they are made of dirt. 
An erie neyon pink glow appears in the distance. 
You walk towards it and climb up a small hill and see that the structure you were in was a colosseum.
Glancing at the pink glow, you see a grid of neyon pink tiles in front of you. """)
    input("Next...")
    player.new_screen()
    print("""Ignoring the tiles, you grab a small pebble that was on the ground under a tree
underground.
╔═══════════════════════════════════════╗
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
║be Whammering the tiles but I want to  ║
║get a new brain                        ║
║                                       ║
║                                       ║
║                                       ║
║Strength +5                            ║
╚═══════════════════════════════════════╝""")
    player.add_item("Stone Berry", 1)
    input("Next...")
    player.new_screen()
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
            player.add_item("Stone Berry", randint(1, 2))
        else:
            print("You got some Wushrooms. ")
            player.add_item("Wushroom", randint(1, 5))
        input("Next...")
        player.new_screen()
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
    player.new_screen()
    print("Suddenly, the floor beneath you burst open and you slide down in to the colosseum.")
    input("Next...")
    player.new_screen()
    print("""A pair of large arms start to grow. 
Dirt around you start flying up towards the arms, forming a dirtstorm. 
You squint your eyes to protect them from the flying debris.
But suddenly it stops. """)
    input("Next...")
    player.new_screen()
    print(""" ____  _      _   _             _          _
|  _ \\(_)_ __| |_(_)_ __   __ _| |__   ___(_)_ __ ___
| | | | | '__| __| | '_ \\ / _` | '_ \\ / _ \\ | '_ ` _ \\
| |_| | | |  | |_| | | | | (_| | | | |  __/ | | | | | |
|____/|_|_|   \\__|_|_| |_|\\__, |_| |_|\\___|_|_| |_| |_|
| |__   __ _ ___    __ ___|___/ _____ | | _____ _ __
| '_ \\ / _` / __|  / _` \\ \\ /\\ / / _ \\| |/ / _ \\ '_ \\
| | | | (_| \\__ \\ | (_| |\\ V  V / (_) |   <  __/ | | |
|_| |_|\\__,_|___/  \\__,_| \\_/\\_/ \\___/|_|\\_\\___|_| |_|""")
    input("Next...")
    dirtingheim = Boss("Dirtingheim", 200, DIRTINGHEIM, player)
    dirtingheim.battle()
    workshop()

def workshop():
    global player
    player.new_screen()
    print("""You enter a ginormous workshop. There are weapons of every kind. 
Swords, Bows, Arrows, Staffs, Quasirhombicosidodecahedron, Gregory Ulveric Nethandral's G.U.Ns, 
Spears, Tridents, Maces, Whips, Spiked Ball On Chain, Daggers, Bombs, Flame-Flingers, Hammers 
and last of all, a bright blue AK47.""")
    input("Next...")
    player.new_screen()
    print("""Wait what?""")
    input("Next...")
    player.new_screen()
    print("""You walk up to the bright blue AK47, ignoring the world ending, Ragnarök worthy 
weaponry around you.""")
    input("Next...")
    player.new_screen()
    print("""You look at the card beneath it and it reads: 
//=============================\\\\
||Property of Hyphen, Creator  ||
||of Conduits. DO NOT TOUCH on ||
||pain of... Wait, nevermind.  ||
||If found mental call: 6349298||
\\\\=============================//""")
    input("Next...")
    player.new_screen()
    print("""A new voice rings in your head, presumibly Hyphen, it says:
'Ah! There's the AK47 I smuggled across the border between the real world.
Oh #!&&@%. What do you mean I'm broadcasting this to the whole of 5AVX?
!#*&@!, #!#*(&), !*&#()! Where is that Dam off switch!
I swear it was next to my Dam! Ah there it is. <Insert loud clanging noises>
Ah fudge, Halbert, I know I'm not meant to bring weapons here but this would make
a new scientific breakthrough. You're not as protective as your Hollowed.
<Insert a metal pipe sound and glass breaking sounds>' And with that, the AK47 disapears.""")
    input("Next...")
    player.new_screen()
    print(f"""You walk away from the weapon rack and see a large vat full of ectoplasma. 
Its shimmering blue glow beckons you. Your {player.small_weapon} falls out of your pocket
(What pockets you ask? Well you don't have them. It was your hammerspace. Don't ask me how
it fell out.) into the large vat. You reach in and pull out a {player.weapon_type}""")
    player.remove_item(player.small_weapon)
    player.add_item(player.weapon_type, 1, LARGE[player.weapon_type])
    player.remove_attacks(SMALL[player.small_weapon])
    input("Next...")
    hallway()

def hallway():
    global player
    player.new_screen()
    print("""You feel a suspicious presence watching you.
You can hear a faint murmuring from the door you entered from.
It sounds like claws on metal.
You see a dark figure in the distance.""")
    input("Next...")
    player.new_screen()
    print("""The air grows colder around you
Skeletr...
Wrong game.
and 
You feel vibrations from deep bellow
The Destroyer has...
Not again!
as if the ground was scared of this creature itself.""")
    input("Next...")
    player.new_screen()
    print("""You dash out of the room and grab one of the daggers on the wall, 
You chuck the dagger at the Suspicious Looking Man.
The dagger flies straight towards the Man but stops and clatters to the ground.""")
    input("Next...")
    player.new_screen()
    speech = input("Input what you want to say >:3 ")
    print(speech)
    input("Next...")
    player.new_screen()
    for _ in range(randint(5, 15)):
        num = randint(1, 50)
        if num == 50:
            if input_sec("Goose ", randint(4, 5), "goose"):
                continue
        elif num % 2:
            if input_sec("Duck ", randint(4, 5), "duck"):
                print("Ducks fall from the sky")
                continue
        elif num % 3:
            if input_sec("Jump ", randint(4, 5), "jump"):
                continue
        else:
            if input_sec("Dodge ", randint(4, 5), "dodge"):
                continue
        print("You hit something in the room")
        input("Next...")
        player.hp -= 20
        player.new_screen()
    player.new_screen()
    print("""You reach the end of a hallway.
An Inconspicuous Flying Ship floats through the ceiling.
a figure jumps out of the cockpit.
It is a duck with a dark red crown on it's head.
╔═══════════════════════════════════════╗
║King Duck IV and The Suspicious Looking║
║                 Man                   ║
║This King Duck IV appears to command an║
║army of ducks. I know he's the fourth  ║
║cus his crown says it. He also seems to║
║command The Suspicious Looking Man who ║
║seems to act as a down hand man.       ║
║                                       ║
║As I write this down, I know they are  ║
║going to kill me as my greatest        ║
║acheivement seems to be killing a pile ║
║of dirt. I probably should be running  ║
║as King Duck IV is making a speech but ║
║I'm lazy. Also it's cute.              ║
║                                       ║
║                                       ║
║                                       ║
║ O                                     ║
║/|\\                                    ║
║/ \\                                    ║
╚═══════════════════════════════════════╝""")
    input("Next...")
    player.new_screen()
    print("""You feel an evil presence watching you.
The Eye of Cuthul...
I SAID WRONG GAME.
You turn around and see the Suspicious Looking Man behind you.
You wave at him and he waves back while drinking a cup of teh A*.
'So that's how he's so good at chasing me. '
You think before realising that not only has he blocked off your only way out, 
but his tea has also gotten an A* in its exams. """)
    input("Next...")
    player.new_screen()
    print("""As the army of ducks advance, you turn and once again, 
something falls out of your pocket.
It's the Earth stone.
'I need new pockets' you think before the ground below you cracks open
and shards of rocks are shot out of the floor impailing absolutely nothing.
as you fall into the crevice, your Whammer starts to release spores that form a portal
to a new green land. which you fall head first through before blacking out...""")
    print(""".----------------------------------------.
|               ___  __      __   ___    |
|                |  /  \\    |__) |__     |
|                |  \\__/    |__) |___    |
|                                        |
| __   __       ___              ___  __ |
|/  ` /  \\ |\\ |  |  | |\\ | |  | |__  |  \\|
|\\__, \\__/ | \\|  |  | | \\| \\__/ |___ |__/|
'----------------------------------------'












Halbert's note: I need to get a new narrator.""")
