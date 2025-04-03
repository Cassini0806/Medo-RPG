from assets.events import *
import sys
from time import sleep

class Gameloop():
    def __init__(self):
        pass

    run = True   
    width = 50

    def Start(self):
        words = "You were trapped in a castle for five days and nights by your vampire girlfriend. You chose freedom and now your life is in danger."
        for char in words:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")
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
        print(f"""                    ██████  ██████   ██████  
                    ██   ██ ██   ██ ██       
                    ██████  ██████  ██   ███ 
                    ██   ██ ██      ██    ██ 
                    ██   ██ ██       ██████  
                         """.center(self.width))
        print("")
        print("       Press Start".center(self.width))
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        player().name()
        input("> ")
        npcs().crow()
        self.loop()

    def randevent(self):
        dice = random.randint(1, 10)        
        if dice > 0 and dice <= 5:
            control().start_fight()
        elif dice > 5 and dice <= 8 :
            loot().loot_open()
        else:
            npcs().spawn_npc()

    def loop(self):
        while self.run == True and player().player["hp"] > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            if player().player["hp"] >= 0:
                key = input("$> ")
                if key == "exit":
                    self.run = False
                    print("Thanks for playing")
                elif key == "nxt":
                    pass
                else:
                    control().terminal(key)
            else:
                print("")
            print(text().text_generator())
            self.randevent()

class control:
    def __init__(self):
        pass    

    def start_npc(self):
        dice = random.choice(Npc_types)
        if dice == Npc_types[0] and player().player["coins"]:
           npcs().butler()

    def start_fight(self):
        dice = random.randint(1, 20)
        if player().player["MobsKilled"] >= 50 and dice == 1:
            Mobspawner().monster.clear()
            Mobspawner().spawn_boss(random.randint(0,2))
            battle(0, True).loop()
        elif player().player["MobsKilled"] >= 200 and player().player["MobsKilled"] < 210:
            Mobspawner().monster.clear()
            Mobspawner().spawn_boss(4)
        else:    
            nMobs = random.randint(1,2)
            Mobspawner().spawn_mob(nMobs)
            print(f"{nMobs} Monsters have spawned, select your target (id or run)")
            while len(Mobspawner().monster) > 0:
                Mobspawner().show_mobs()
                select = input("> ")
                if select.isdigit():
                    slct = int(select) - 1
                    if slct < len(Mobspawner().monster) and slct >= 0 and player().player["hp"] > 0:
                        battle(slct, False).loop()
                        print(f"There are {len(Mobspawner().monster)} Mobs left")
                        print("")
                        pass
                    else:
                        pass
                elif select == "run":
                    Mobspawner().monster.clear()
                    break
                else:
                    print("Mob doesn't exist")
                    pass
        input("> ")


    def edit_inventory(self):
        plin = inventory()
        plin.show_inventory()
        print(f"\033[32mCommands: drop, exit, use, offhand, offartc\033[0m")
        key = input("inventory> ")
        if key == "exit":
            pass
        elif key == "drop":
            plin.del_item()
            self.edit_inventory()
        elif key == "use":
            plin.use_item()
            self.edit_inventory()
        elif key == "offhand":
            player().off_hand()
        elif key == "offartc":
            player().amulet()
        else:
            print("\033[31mCommand not founded\033[0m")
            self.edit_inventory()

    def terminal(self, key):
        key = key
        if key == "inv":
            self.edit_inventory()
            self.terminal(input("> "))
        elif key == "stats":
            player().show_player()
            self.terminal(input("> "))
        elif key == "help":
            help().help()
            self.terminal(input("> "))
        elif key == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            self.terminal(input("> "))
        elif key == "nxt":
            pass
        else:
            print(f"{Npc_types[0]}: \033[31mCommand not founded, please type help for commands\033[0m")
            self.terminal(input("> "))

Gameloop().Start()
