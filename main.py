from assets.events import *

class control:
    def __init__(self):
        pass    
    
    def edit_inventory(self):
        plin = inventory()
        plin.show_inventory()
        print(f"\033[32mCommands: add, drop, exit, use, offhand, offartc\033[0m")
        key = input("inventory> ")
        if key == "exit":
            pass
        elif key == "drop":
            plin.del_item()
            self.edit_inventory()
        elif key == "add":
            t = list(input("inv_add> "))
            h = int(t[0])
            i = int(t[1])
            plin.add_item(h, i)
            os.system('cls' if os.name == 'nt' else 'clear')
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

    def terminal(self):
        key = input("> ")
        if key == "inv":
            self.edit_inventory()
            self.terminal()
        elif key == "stats":
            player().show_player()
            self.terminal()
        elif key == "help":
            print(f"\033[32mAvaliable commands: exit, help, inventory, stats\033[0m")
            self.terminal()
        elif key == "exit":
            print("Thanks for playing")
            pass
        elif key == "cls":
            os.system('cls' if os.name == 'nt' else 'clear')
            self.terminal()
        elif key == "battle":
            Mobspawner().spawn_mob(1)
            battle(0, False).loop()
            self.terminal()
        else:
            print("\033[31mCommand not founded, please type help for commands\033[0m")
            self.terminal()

Tower().Start()
control().terminal()