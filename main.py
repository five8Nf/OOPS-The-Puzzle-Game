import os
from inputimeout import inputimeout, TimeoutOccurred
from Stages import *

from player import *

intro()
loading()
to = room1()
while to != "left" and to != "right":
    input(f"{to} is not a valid input")
    clear_screen()
    to = input("Do you want to go left or right? ")
if to == "left":
    left()
elif to == "right":
    pillar_puzzle()
    Whammer()