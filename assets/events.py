import random
import os
from assets.lists import *

class player:

    player = {
        "gender": "m",
        "hp": 100,
        "atk": 2,
        "xp": 0,
        "hpMax": 100,
        "coins": 0,
        "name": "Player",
        "level": 1,
        "amulet": [""],
        "hand": [""],
        "xpMax": 100,
    }

    def name(self):
        print("Select your attributes, please.")
        self.player["name"] = input("Name: ")
        self.player["gender"] = input("Gender [m/f]: ")

    def show_player(self):    
        keys = list(self.player.keys())
        index = 0
        print(f"\033[31m{self.player["name"]}")
        print(f"\033[34m  Level: {self.player["level"]}\033[0m")
        print(f"\033[34m  Hand: {self.player["hand"][0]}\033[0m")
        print(f"\033[34m  Artifact: {self.player["amulet"][0]}\033[0m")
        while index <= len(self.player) - 7:
            print(f"\033[32m  {keys[index]}: {self.player[keys[index]]}\033[0m")
            index += 1        

    def off_hand(self):
        if self.player["hand"] != [""]:
            inventory().inventory.append(self.player["hand"])
            self.player["hand"] = [""]
            self.player["atk"] = 2
        else: 
            print("No item is in your hand")

    def amulet(self):
        if self.player["amulet"] != [""]:
            inventory().inventory.append(self.player["amulet"])
            self.player["amulet"] = [""]
            self.player["hp"] = 100 * self.player["level"]
        else: 
            print("No Artifact in use")

class inventory:
    def __init__(self):
        pass    

    inventory = [["Sword", 15, 0, 1],
                 ["Axe", 20, 0, 1],
                 ["Apple", 5, 1],
                 ["Sword", 15, 0, 1],
                 ["Gun", 50, 0, 1],
                 ["Oil Lamp", 15, 3],
                 ]

    def show_inventory(self):
        print(f"\033[31mInventory\033[0m")
        if len(self.inventory) > 0:
            index = 0
            for i in self.inventory:
                index += 1
                print(f"\033[34m {index} - {i[0]}\033[0m")
        else:
            print("The inventory is empty")

    def del_item(self):
        j = input("inv_drop> ")
        if j.isdigit():
            i = int(j) - 1
            if i < len(self.inventory):
                j = int(i)
                self.inventory.pop(j)
            else:
                pass
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Item not founded")

    def add_item(self, h, i):
        self.inventory.append(items[h][i])

    def use_item(self):
        j = input("inv_use> ")
        if j.isdigit():
            i = int(j) - 1
            if i < len(self.inventory):
                if self.inventory[i][2] == 0 and player().player["hand"] == [""]:
                    player().player["atk"] = self.inventory[i][1] * 2
                    player().player["hand"] = self.inventory[i]
                    self.inventory.pop(i)
                    os.system('cls' if os.name == 'nt' else 'clear')
                elif self.inventory[i][2] == 1 and player.player["hp"] < player().player["hpMax"]:
                    player().player["hp"] += self.inventory[i][1]
                    self.inventory.pop(i)
                    os.system('cls' if os.name == 'nt' else 'clear')
                elif self.inventory[i][2] == 3 and player().player["amulet"] == [""]:
                    player().player["hpMax"] += self.inventory[i][1] * 3
                    player().player["amulet"] = self.inventory[i]
                    self.inventory.pop(i)
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    pass    
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
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

    def spawn_boss(self, id_boss):
        level = self.Playerlevel * 20
        new_boss = {
            "name": Boss[id_boss],
            "level": "",
            "hp": 25 * level,
            "atk": 2 * level,
            "xp": 2 * level
        }
        self.monster.append(new_boss)

class battle:
    def __init__(self, id_mob, Boss):
        self.id_mob = int(id_mob)
        self.IsBoss = Boss
        self.MobName = Mobspawner().monster[self.id_mob]["name"]
        self.MobLevel = Mobspawner().monster[self.id_mob]["level"]
        self.width = 100

    def drop_item(self):
        c = random.randint(1, 3)
        if c == 1:
            drop = items[random.randint(0,3)][random.randint(0,4)]
            inventory().inventory.append(drop)
            print(f"New item obteined: {drop[0]}")
        else:
            pass

    def level_up(self):
        if player().player["xp"] >= player().player["xpMax"]:
            player().player["xp"] -= player().player["xpMax"]
            player().player["level"] += 1
            player().player["hpMax"] += 100

    def attack_player(self):
        player().player["hp"] -= Mobspawner.monster[self.id_mob]["atk"] 

    def attack_mob(self):
        Mobspawner.monster[self.id_mob]["hp"] -= player().player["atk"]  
        self.attack_player()

    def show_battle(self):
        print(f"\033[34mPlayer // Hp: {player().player["hp"]}\033[31m".center(self.width))
        print(f"{self.MobName}{self.MobLevel} // Hp:{Mobspawner().monster[self.id_mob]["hp"]}\033[0m".center(self.width))

    def loop(self):
        while Mobspawner().monster[self.id_mob]["hp"] > 0 and player().player["hp"] > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.show_battle()
            command = input("Next Movement: ")
            if command == "atk":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.attack_mob()
                if player().player["hp"] <= 0:
                    print(f"\033[31mYou died\033[0m".center(50))
                    break
                elif Mobspawner().monster[self.id_mob]["hp"] <= 0:
                    player().player["xp"] += Mobspawner().monster[self.id_mob]["xp"]
                    print(f"\033[32m{self.MobName} as been slayed".center(self.width))
                    print(f"Hp: {player().player["hp"]} // Xp: {player().player["xp"]}\033[0m".center(self.width))
                    Mobspawner().monster.pop(self.id_mob)
                    self.drop_item()
                    self.level_up()
                    break
            elif command == "run" and self.IsBoss == False:
                os.system('cls' if os.name == 'nt' else 'clear')
                player().player["xp"] += Mobspawner().monster[self.id_mob]["xp"]
                Mobspawner().monster.pop(self.id_mob)
                print(f"\033[31mYou ran away from {self.MobName}".center(self.width))
                print(f"Hp: {player().player["hp"]} // Xp: {player().player["xp"]}\033[0m".center(self.width))
                break
            elif command == "inv":
                inventory().show_inventory()
                print(f"\033[32mCommands: offhand, use\033[0m")
                inv = input("inv> ")
                if inv == "use":
                    inventory().use_item()
                elif inv == "offhand":
                    player().off_hand()
                else:
                    pass
            else:
                pass

class npcs:
    def __init__(self):
        pass    
    
    def upgrade_tool(self):
        id_item = input("Upgrade_Item> ")
        if id_item.isdigit():
            id = int(id_item) - 1
            level = inventory().inventory[id][3] + 1
            inventory().inventory[id][3] += 1
            inventory().inventory[id][1] * 2
            inventory().inventory[id][0] = inventory().inventory[id][0] + f" l{level}"
            player().player["coins"] -= level ** 2
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Item not founded")

    def sell_item(self):
        i = input("inv_sell> ")
        if i.isdigit():
            i = int(i) - 1
            if i < len(inventory().inventory):
                j = int(i)
                player().player["coins"] += inventory().inventory[j][1] * 2
                inventory().inventory.pop(j)
            else:
                pass
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Item not founded")
    
class Tower:
    def __init__(self):
        pass
    
    width = 50
    
    def Start(self):
        text = "The Tower"
        print(text.center(self.width))
        print(f"You were trapped in a tower for five days and fives nights by your girlfriend.")
        print(f"You chose freedom and now your life is in danger.")
        print("")
        print(f"""          ▄▄▄▄███▄▄▄▄      ▄████████ ████████▄   ▄██████▄  
        ▄██▀▀▀███▀▀▀██▄   ███    ███ ███   ▀███ ███    ███ 
        ███   ███   ███   ███    █▀  ███    ███ ███    ███ 
        ███   ███   ███  ▄███▄▄▄     ███    ███ ███    ███ 
        ███   ███   ███ ▀▀███▀▀▀     ███    ███ ███    ███ 
        ███   ███   ███   ███    █▄  ███    ███ ███    ███ 
        ███   ███   ███   ███    ███ ███   ▄███ ███    ███ 
         ▀█   ███   █▀    ██████████ ████████▀   ▀██████▀  
                                                        """.center(self.width))