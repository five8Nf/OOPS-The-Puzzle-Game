import os
from inputimeout import inputimeout, TimeoutOccurred
from Stages import *

from player import *

intro()
loading()
next = room1()
while next != "left" and next != "right":
    next = input("Do you want to go left or right? ")
if next == "left":
    left()
elif next == "right":
    pillar_puzzle()