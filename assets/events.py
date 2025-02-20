import random
import os
from assets.lists import *

class player:

    player = {
        "name": "Player",
        "gender": "",
        "level": 1,
        "hp": 100,
        "hpMax": 100,
        "xp": 0,
        "xpMax": 50,
        "hand": [""],
        "atk": 2,
        "aureus": 0,
    }

    def name(self):
        print("Select your attributes, please.")
        self.player["name"] = input("Name: ")
        self.player["gender"] = input("Gender [m/f]: ")

    def show_player(self):    
        print(f"\033[31m{self.player["name"]}")
        print(f"\033[34m  Level: {self.player["level"]}")
        print(f"\033[32m  Hp: {self.player["hp"]}")
        print(f"  Xp: {self.player["xp"]}")
        print(f"  hand: {self.player["hand"][0]}")
        print(f"  atk: {self.player["atk"]}")
        print(f"  Aureus: {self.player["aureus"]}\033[0m")

    def off_hand(self):
        if self.player["hand"] != [""]:
            inventory().inventory.append(self.player["hand"])
            self.player["hand"] = [""]
            self.player["atk"] = 2
        else: 
            print("No item is in your hand")

class inventory:
    def __init__(self):
        pass    

    inventory = [["sword", 15, 0],
                 ["axe", 20, 0],
                 ["apple", 5, 1],
                 ["sword", 15, 0],]

    def show_inventory(self):
        print(f"\033[31mInventory\033[0m")
        if len(self.inventory) > 0:
            for i in self.inventory:
                print(f"\033[34m * {i[0]}\033[0m")
        else:
            print("The inventory is empty")

    #search the item by name and return the index
    def search(self, l):
        for j in range(len(self.inventory)-1):
            if l in self.inventory[j]:
                return j

    def del_item(self, i):
        j = self.search(i)
        if i in self.inventory[j]:
            self.inventory.pop(j)

    def add_item(self, h, i):
        self.inventory.append(items[h][i])

    def use_item(self, j):
        i = self.search(j)
        if self.inventory[i][2] == 0 and player().player["hand"] == [""]:
            player().player["atk"] = self.inventory[i][1] * 2
            player().player["hand"] = self.inventory[i]
            self.inventory.pop(i)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif self.inventory[i][2] == 1 and player.player["hp"] < player().player["hpMax"]:
            player().player["hp"] += self.inventory[i][1]
            self.inventory.pop(i)
            os.system('cls' if os.name == 'nt' else 'clear')
        else: 
            print("Item not found")

class Mobspawner:
    def __init__(self):
        self.Playerlevel = player().player['level']

    monster = []

    def create_mob(self):
        level = self.Playerlevel * random.randint(1, 10)
        new_mob = {
            "name": random.choice(Mob_types),
            "level": level,
            "hp": 10 * level,
            "atk": 3 * level,
            "xp": 3 * level
        }
        return new_mob

    def spawn_mob(self, n_mob):
        for i in range(n_mob):
            new_mob = self.create_mob()
            self.monster.append(new_mob)

    def show_mobs(self):
        for i in range(len(self.monster)):
            print(f"{self.monster[i]}")

class battle:
    def __init__(self, id_mob):
        self.id_mob = int(id_mob)
        self.PlayerLevel = player().player["level"]
        self.PlayerHP = player().player["hp"]
        self.PlayerAtk = player().player["atk"]
        self.PlayerXp = player().player["xp"]
        self.MobName = Mobspawner().monster[self.id_mob]["name"]
        self.MobLevel = Mobspawner().monster[self.id_mob]["level"]
        self.MobHP = Mobspawner().monster[self.id_mob]["hp"]
        self.MobAtk = Mobspawner().monster[self.id_mob]["atk"]
        self.MobXp = Mobspawner().monster[self.id_mob]["xp"]
    
    def attack_player(self):
        self.PlayerHP -= self.MobAtk
    
    def attack_mob(self):
        self.MobHP -= self.PlayerAtk
        self.attack_player()

    def show_battle(self):
        print(f"\033[34mPlayer // Hp: {self.PlayerHP}\033[31m")
        print(f"{self.MobName} level {self.MobLevel} // Hp:{self.MobHP}\033[0m")

    def loop(self):
        while self.MobHP > 0 and self.PlayerHP > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.show_battle()
            command = input("Next Movement: ")
            if command == "atk":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.attack_mob()
                if self.PlayerHP <= 0:
                    print(f"\033[31mYou died\033[0m")
                elif self.MobHP <= 0:
                    self.PlayerXp += self.MobXp
                    print(f"\033[32m{self.MobName} as been slayed")
                    print(f"Hp: {self.PlayerHP} // Xp: {self.PlayerXp}\033[0m")
            elif command == "run":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.PlayerXp -= self.MobXp
                print(f"\033[31mYou ran away from {self.MobName}")
                print(f"Hp: {self.PlayerHP} // Xp: {self.PlayerXp}\033[0m")
                break
            elif command == "inv":
                inventory().show_inventory()
                print(f"\033[32mCommands: offhand, use\033[0m")
                inv = input("inv> ")
                if inv == "use":
                    i = int(input("inv_use> "))
                    inventory().use_item(i)
                elif inv == "offhand":
                    player().off_hand()
                else:
                    pass
            else:
                pass
            