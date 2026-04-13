from Attacks import Attack

# && = insert opponent name
# ** = insert weapon name
# :: = insert roll number

PUNCH = Attack("Punch", ["punched"], 5, 10, 0.3)
KICK = Attack("Kick", ["kicked"], 3, 15, 0.2)
SARCASM = Attack("Sarcasm", ["used sarcasm on"], 1, 100, 0.1)

BASIC = {PUNCH, KICK, SARCASM}

BONK = Attack("Bonk", ["Bonked"], 10, 15, 0.7)
TOSS = Attack("Toss", ["Tossed", "their", "whammer" "at"], 15, 20, 0.4)
WHAMMER = {BONK, TOSS}

THROW = Attack("Throw", ["threw",  "their", "**", "at"], 15, 20, 0.4)
POMMEL = Attack("Pommel Hit", ["hit", "&&", "with", "pommel"], 10, 17, 0.75)
WHACK = Attack("Whack", ["whacked"], 10, 17, 0.75)
SWING = Attack("Swing", ["swung", "short", "branch", "at"], 10, 17, 0.75)
ROLL = Attack("Roll D12", ["rolled", "a", "::"],8 ,20 , "X")

SMALL = {"Handle" : {THROW, POMMEL}, 
         "Thin Stick" : {THROW, WHACK}, 
         "Short Stick" : {THROW, SWING}, 
         "Dodecahedron" : {THROW, ROLL}}

# SLASH = Attack("Slash", ["slashed", "at"], 20, 30, 0.6)
# STAB = Attack("Stab", ["stabbed"], 20, 25, 0.7)

# SWORD = {SLASH, STAB}

# SHOOT = Attack("Shoot", ["shot", "at"], 23, 35, 0.5)
# STAB_WITH_ARROW = Attack("Stab with arrow", ["Stabbed"], 20, 25, 0.7)

# BOW = {SHOOT, STAB_WITH_ARROW}


ROCKSLIDE = Attack("Rock Slide", ["Rocks", "fell", "from", "the", "sky"],30 ,35 , 0.1)
EARTHQUAKE = Attack("Earthquake", ["Caused", "an", "earthquake"], 10, 15, 1)

DIRTINGHEIM1 = {ROCKSLIDE, EARTHQUAKE}