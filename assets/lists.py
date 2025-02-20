items = [
    [
        ["sword", 15, 0],
        ["axe", 20, 0],
        ["spear", 10, 0],
        ["dagger", 5, 0],
        ["gun", 100, 0],   
    ],
    [
        ["lemon", 1, 1],
        ["apple", 5, 1],
        ["bread", 10, 1],
        ["meat", 25, 1],
        ["cake", 50, 1],
    ],
]

Artifacts = {
    "ring": 50,
    "crucifix": 25,
    "cricket": 10,
    "rubik's cube": 15,
}


Miscellaneous = {
    "quartz": 5,
    "wood": 10,
    "book": 25,
}

Mob_types = (
    "Ghost",
    "Goblin",
    "Skeleton",
    "Gargoyle",
    "Devil Tree",
    "Witch",
)

Boss = (
    "Dragon",
    "Necromancer",
)

Npc_types = (
    "Blacksmith",
    "Butcher",
    "Farmer",
    "Librarian",
    "Priest",
    "Warrior",
)

def logo():
    print(f"""   ▄▄▄▄███▄▄▄▄      ▄████████ ████████▄   ▄██████▄  
    ▄██▀▀▀███▀▀▀██▄   ███    ███ ███   ▀███ ███    ███ 
    ███   ███   ███   ███    █▀  ███    ███ ███    ███ 
    ███   ███   ███  ▄███▄▄▄     ███    ███ ███    ███ 
    ███   ███   ███ ▀▀███▀▀▀     ███    ███ ███    ███ 
    ███   ███   ███   ███    █▄  ███    ███ ███    ███ 
    ███   ███   ███   ███    ███ ███   ▄███ ███    ███ 
    ▀█   ███   █▀    ██████████ ████████▀   ▀██████▀  
                                                        """)
