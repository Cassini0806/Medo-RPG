import random
from assets.lists import *

player = {
    "name": "",
    "gender": "",
    "level": 1,
    "hp": 100,
    "hpMax": 100,
    "Xp": 0,
    "XpMax": 50,
    "atk": 2 * item["nuke"]
}

monsters = []

def create_mob():
    level = player["level"] * random.randint(1, 2)
    new_mob = {
        "name": random.choice(Npc_types),
        "level": level,
        "hp": 10 * level,
        "atk": 5 * level,
        "xp": 2 * level
    }
    return new_mob

def spawn_mob(n_mob):
    for x in range(n_mob):
        new_mob = create_mob()
        monsters.append(new_mob)

def show_mobs():
    for mob in monsters:
        print(f"Name: {mob['name']} // Level: {mob['level']} // Hp: {mob['hp']}")

        nomes = ["Carlos", "Ana", "Pedro", "Bruno"]
