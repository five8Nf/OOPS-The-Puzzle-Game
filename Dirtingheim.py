from Stages import get_player, new_screen, dirtingheim_appearence
from Attack_list import DIRTINGHEIM

max_health = 200
health_remaining = 200

def round_top():
    global max_health, health_remaining
    new_screen()
    hp_percent = health_remaining / max_health * 100
    bar_length = 40
    filled_length = int(bar_length * hp_percent / 100)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    print(f"""Dirtingheim HP: {health_remaining:.1f}/{max_health:.1f} ({hp_percent:.1f}%) [{bar}]
\n============================================================================================\n""")

def battle():
    player = get_player()
    while True:
        round_top()
        