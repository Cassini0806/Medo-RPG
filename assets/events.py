import random
import os
from assets.lists import *

class player:

    player = {
        "gender": "m",
        "hp": 90,
        "atk": 2,
        "xp": 0,
        "coins": 100,
        "name": "Player",
        "level": 1,
        "amulet": [""],
        "hand": [""],
        "xpMax": 100,
        "hpMax": 100,
        "MobsKilled": 0
    }

    def name(self):
        print("Select your name and gender, please.")
        self.player["name"] = input("Name: ")
        gender = input("Gender [m/f]: ")
        if gender == "m" or gender == "f":
            self.player["gender"] = gender
        else:
            print("Huh...ok?")
            self.player["gender"] = gender

    def show_player(self):    
        keys = list(self.player.keys())
        index = 0
        print(f"\033[31m{self.player["name"]}")
        print(f"\033[34m  Level: {self.player["level"]}\033[0m")
        print(f"\033[34m  Hand: {self.player["hand"][0]}\033[0m")
        print(f"\033[34m  Artifact: {self.player["amulet"][0]}\033[0m")
        while index <= len(self.player) - 8:
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

    inventory = [["Bread", 15, 1],]

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
            print("Item not found")

    def use_item(self):
        j = input("inv_use> ")
        if j.isdigit():
            i = int(j) - 1
            if i < len(self.inventory) and i >= 0:
                if self.inventory[i][2] == 0 and player().player["hand"] == [""]:
                    player().player["atk"] = self.inventory[i][1] * 2
                    player().player["hand"] = self.inventory[i]
                    self.inventory.pop(i)
                    os.system('cls' if os.name == 'nt' else 'clear')
                elif self.inventory[i][2] == 1 and player.player["hp"] < player().player["hpMax"]:
                    health = player().player["hp"] * self.inventory[i][1] / 10
                    player().player["hp"] += health
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
        level = self.Playerlevel * random.randint(1, 5)
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
            print(f"{i + 1} - {self.monster[i]["name"]} lvl {self.monster[i]["level"]}")

    def spawn_boss(self, id_boss):
        level = self.Playerlevel * 15
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
        if c >= 1 and c <= 2:
            drop = items[random.randint(0,2)][random.randint(0,5)]
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
            if self.IsBoss == True:
                print(f"You found {Mobspawner().monster[self.id_mob]["name"]}")
            self.show_battle()
            command = input("Next Movement: ")
            if command == "atk":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.attack_mob()
                if player().player["hp"] <= 0:
                    print(f"\033[31mYou died\033[0m".center(50))
                    Mobspawner().monster.clear()
                    break
                elif Mobspawner().monster[self.id_mob]["hp"] <= 0:
                    player().player["xp"] += Mobspawner().monster[self.id_mob]["xp"]
                    player().player["MobsKilled"] += 1
                    print(f"\033[32m{self.MobName} as been slayed".center(self.width))
                    if Mobspawner.monster[0]["name"] == Boss[4]:
                        print("Congratulations!".center(self.width))
                        player().player["hp"] -= player().player["hp"]
                    else:
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
    
    def spawn_npc(self):
        dice = random.randint(1,2)
        print(f"You met {Npc_types[dice]}")
        if dice == 1:
            self.butler()
        else:
            self.lady()

    def upgrade_tool(self):
        inventory().show_inventory()
        id_item = input("Upgrade_Item> ")
        if id_item.isdigit():
            id = int(id_item) - 1
            if inventory().inventory[id][2] == 0 or inventory().inventory[id][2] == 3:
                level = inventory().inventory[id][3] + 1
                inventory().inventory[id][3] += 1
                inventory().inventory[id][1] * 2
                inventory().inventory[id][0] = inventory().inventory[id][0] + f" lvl {level}"
                player().player["xp"] -= level ** 2
                print(f"{Npc_types[2]}: Now it's better, i think...")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Npc_types[2]}: I cannot upgrade this, sorry")
                self.upgrade_tool()
        elif id_item == "exit":
            print(f"{Npc_types[2]}: Ok, see you...")
            pass  
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Item not found")

    def trade(self):
        inventory().show_inventory()
        id_item = input("Trade> ")
        if id_item.isdigit():
            id = int(id_item) - 1
            if inventory.inventory[id][2] == 2:
                inventory.inventory.pop(id)
                inventory.inventory.append(items[3][random.randint(0, 5)])
                print("Maybe this would be useful")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Npc_types[2]}: Why would i need this? Do you have something more interesting?")
                self.trade()
        elif id_item == "exit":
            print(f"{Npc_types[2]}: Ok, see you...")
            pass
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Item not found")
            self.trade()

    def sell_item(self):
        inventory().show_inventory()
        i = input("sell> ")
        if i.isdigit():
            i = int(i) - 1
            if i < len(inventory().inventory):
                j = int(i)
                player().player["coins"] += inventory().inventory[j][1] / 5
                inventory().inventory.pop(j)
                print(f"{Npc_types[0]}: It ain't much, but it's honest work")
            else:
                pass
        elif i == "exit":
            pass  
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Item not found")
            self.sell_item()

    itemsB = []
    
    def create_items(self):
        self.itemsB.clear()
        self.itemsB.append(items[0][random.randint(0,2)])
        self.itemsB.append(items[0][random.randint(3,5)])
        self.itemsB.append(items[1][random.randint(0,2)])
        self.itemsB.append(items[1][random.randint(3,5)])
            
    def buy_item(self):
        inventory().show_inventory()
        index = 0
        for i in self.itemsB:
            print(f"{index + 1} - {i[0]} ${i[1] / 5}") 
            index += 1
        i = input("buy> ")
        if i.isdigit(): 
            i = int(i) - 1
            ii = input("Quantity> ")
            if ii.isdigit():
                ii = int(ii)
                if i < len(self.itemsB) and player().player["coins"] >= self.itemsB[i][1] * ii / 10:
                    groceries = i
                    player().player["coins"] -= self.itemsB[groceries][1] / 10
                    for h in range(ii):
                        inventory().inventory.append(self.itemsB[groceries])
                    print(f"{Npc_types[1]}: Please, don't tell this to anyone")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{Npc_types[1]}: You cannot pay for it!")
                    npcs().buy_item()
            else:
                pass
        elif i == "exit":
            pass  
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Item not found")
            npcs().buy_item()

    def butler(self):
        print(f"{Npc_types[1]}: Hello sir, do you need help?(y/n)")
        key = input("> ")
        if key == "y":
            print(f"{Npc_types[1]}: So how can i help you?(sell or buy)")
            ans = input("> ")
            if ans == "sell":
                inventory().show_inventory()
                npcs().sell_item()
            elif ans == "buy":
                npcs().create_items()
                npcs().buy_item()
        else:
            print(f"{Npc_types[1]}: Well, see you later")

    def lady(self):
        print(f"{Npc_types[2]}: Huh, Hello? Do you need my help!?(y/n)")
        key = input("> ")
        if key == "y":
            print(f"{Npc_types[2]}: How can I be helpful?(trade or upt)")
            ans = input("> ")
            if ans == "upt":
                npcs().upgrade_tool()
            elif ans == "trade":
                npcs().trade()
        else:
            print(f"{Npc_types[2]}: Ok, see you...")
            
    def crow(self):
        print(f"{Npc_types[0]}: Hello friend, I'm Jack and i'll help you in these journey.")
        help().first_help()
        
class loot: 
    def __init__(self):
        self.Playerlevel = player().player['level']
        pass

    def spawn_mimic(self):
        Mobspawner().monster.clear()
        level = self.Playerlevel * random.randint(1, 10)
        new_mob = {
            "name": "Mimic ",
            "level": level,
            "hp": 10 * level,
            "atk": 3 * level,
            "xp": 3 * level
        }
        Mobspawner.monster.append(new_mob)

    def open_chest(self):
        dice = random.randint(0,2)
        if dice == 2:
            self.spawn_mimic()
            battle(0, False).loop()
        else:
            drop = items[random.randint(0,2)][random.randint(0,5)]
            print(f"You have found {drop[0]}")
            inventory().inventory.append(drop)
            input("> ")


    def loot_open(self):
        print(f"You found a {random.choice(box)}.")
        print("Do you want to open it?[y/n]")
        ans = input("> ")
        if ans == "y":
            self.open_chest()
        else: 
            pass

class help:
    def __init__(self):
        pass

    def first_help(self):
        print(f"{Npc_types[0]}: The first thing you to need know is: the castle is full of creatures ready to murder you.")
        print(f"You can fight with them, but be careful. You will need weapons and resources to escape from here, like this dagger.")
        inventory().inventory.append(items[0][1])
        print(f"{Npc_types[0]}: Do you need know more?(y/n)")
        help = input("> ")
        if help == "y":
            self.help()
        else:
            print(f"{Npc_types[0]}: Right, i'll be here if you need help!")
            input("> ")
            pass

    def help(self):
        print(f"{Npc_types[0]}: Type what do you need know. (commands, npcs, battles, inventory, items, stats)")
        help = input("> ")
        if help == "commands":
            self.help_Command()
        elif help == "npcs":
            self.help_Npcs()
        elif help == "battles":
            self.help_battles()
        elif help == "inventory":
            self.help_inventory()
        elif help == "items":
            self.help_items()
        elif help == "stats":
            print(f"{Npc_types[0]}: Are your stats like level, attack and health points. I thought you knew that.")
         elif help == "credits":
            print(f"This game was designed and programmed by Thiago Cardoso. Please access my portfolio on github at \033[34m'https://github.com/Cassini0806'\033[0m")
        else:
            print(f"{Npc_types[0]}: I don't know what this is. Please enter another command.")
            self.help()
        input("> ")

    def help_items(self):
        print(f"{Npc_types[0]}: There are several different items for different functions.")
        print(f"    Weapons: can increase damage to mobs;")
        print(f"    Food: can regenerate health points;")
        print(f"    Broken items: can be traded to the Lady in the mirror for artifacts;")
        print(f"    Artifacts: are amulets that increase health points.")

    def help_inventory(self):
        print(f"{Npc_types[0]}: The inventory is where you can acess and manage your items.")
        print(f"In the inventory, you have some special commands:")
        print(f"    drop: delete the item;")
        print(f"    use: use the item for regeneration or increase atk/hp;")
        print(f"    offhand: remove weapons of your hand;")
        print(f"    offartc: remove artifacts from the other hand.")

    def help_battles(self):
        print(f"{Npc_types[0]}: It's fight or flight, you can battle with monsters or run of then.")
        print(f"During a fight, you can attack using 'atk' or acess the inventory using 'inv'. You can flight of a fight using 'run' (except boss fights).")

    def help_Npcs(self):
        print(f"{Npc_types[0]}: Npcs are ready for help you, they can trade, sell, buy and even upgrading items.")
        print(f"But remember, they will charge coins or xp for the services.")

    def help_Command(self):
        print(f"{Npc_types[0]}: Here are some commands to you:")
        print("     inv: acess your inventory;")
        print("     stats: acess your stats (hp, atk, etc);")
        print("     exit: close the game, inventory or npc dialogue;")
        print("     (You can only close the game after a complete turn marked by the '$>' symbol)")
        print("     nxt: go to the next event.")

class text:
    def __init__(self):
        pass

    def text_generator(self):
        text = random.choice(frases)
        new_text = text.replace("{$$$}", random.choice(room))
        return new_text
