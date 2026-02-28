import os
from inputimeout import inputimeout, TimeoutOccurred

from player.py import *

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")