import os
from time import sleep
from random import randint
from inputimeout import inputimeout, TimeoutOccurred

from Boss import *
from Attack_list import *
from Player import *
from Ascii_things import *
from String_formating import *

player = None

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
    print("The Puzzle Game Chapter 2")
    print("Loading world")
    sleep(1)
    clear_screen()
    print("The Puzzle Game Chapter 2")
    print("Loading world.")
    sleep(1)
    clear_screen()
    print("The Puzzle Game Chapter 2")
    print("Loading world..")
    sleep(1)
    clear_screen()
    print("The Puzzle Game Chapter 2")
    print("Loading world...")
    sleep(1)
    clear_screen()
    print("The Puzzle Game Chapter 2")
    print("Loading world..")
    sleep(1)
    clear_screen()
    print("The Puzzle Game Chapter 2")
    print("Loading world.")
    sleep(1)
    clear_screen()
    print("The Puzzle Game Chapter 2")
    print("Loading world")
    sleep(1)

def intro():
    global player
    clear_screen()
    print(ascii_text_chap1[0])
    sleep(5)
    clear_screen()
    print(ascii_text_chap1[1])
    print(ascii_text_chap2[0])
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
    weapon = input("Please input the number of your previous weapon (1.Sword, 2.Bow, 3.Staff or 4.Quasirhombicosidodecahedron): ")
    while not weapon in WEAPONS.keys():
        weapon = input(f"{weapon} not a valid number. Input your previous weapon:(1.Sword, 2.Bow, 3.Staff or 4.Quasirhombicosidodecahedron):")
    player.weapon_choice(WEAPONS[weapon])
    clear_screen()
    print("The Puzzle Game")
    print(f"Welcome Back {name}")
    sleep(5)
    loading()

def beginning():
    player.new_screen()
    print("""You wake up under a deep green canopy. 
Birds chirp incessently and a strong scent of rotting mushrooms fills the air. 
    Good you're better than Redacted, Gother.
You blink through the warm blinding sunlight and spot a small backpack lying on the floor. """)
    input("Next...")
    player.new_screen()
    print("""You open the windback... I mean the backpack expecting to see
the things that you have collected in the temple but you only find your journal. """)
    input("Next...")
    player.new_screen()
    print("""you see a strange Rabbit in the distance. 
The mysterious voice in your head, That's me :D, says that it is a
Violent Violet Rabbit Wielding Violins Violenty. 
You think, awww right before it jumps and starts playing horrific violin music.
Your ears start bleeding and you throw a rock at the rabbit to get it to stop. 
However, your rock misses and hits the branch above knocking
your ectoplasmic weapon out.
Blood splatters everywhere as the sharp part of the weapon
plunges into the rabbit's neck. 
What's wrong Halbert? Why are you look so traumatised?
Anyways, as I was saying, 
Blood splatters every where and your weapon is coated red. """)
    input("Next...")
    player.new_screen()
    print("""Why are you just standing still?
I suggest you walk up and remove the rabbit's entr...
Ack! Halbert give me back the mic.
<Insert loud thump>""")
    input("One long therapy session later...")
    player.new_screen()
    print("""    Ok I've locked that madman up and I now will do the narration. 
    You stood there staring in horror for so long that the rain washes away the blood
    and the rabbits disolves into violin music. 
    you pick up your weapon and then see your Earthstone right beside it.""")
    input("Next...")
    player.add_item(WEAPONS[weapon], 1, LARGE[WEAPONS[weapon]])
    ROCKSLIDE.change_accuracy(0.7)
    player.add_item("Earthstone", 1, DIRTINGHEIM)
    player.new_screen()
    print("""In the distance,  you see a smoke plume and realise that that is """)