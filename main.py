from assets.events import *

class control:
    def __init__(self):
        pass    
    
    def edit_inventory(self):
        plin = inventory()
        plin.show_inventory()
        print(f"\033[32mCommands: add, del, exit, use, offhand\033[0m")
        key = input("inventory> ")
        if key == "exit":
            pass
        elif key == "del":
            i = input("inventory_del> ")
            plin.del_item(i)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"The item '{i}' was removed")
            self.edit_inventory()
        elif key == "add":
            t = list(input("inventory_add> "))
            h = int(t[0])
            i = int(t[1])
            #plin.add_item(h, i)
            self.edit_inventory()
        elif key == "use":
            i = input("inventory_use> ")
            plin.use_item(i)
            self.edit_inventory()
        elif key == "offhand":
            player().off_hand()
        elif key == "ggg":
            l = input("")
            plin.search(l)
        else:
            print("\033[31mCommand not founded\033[0m")
            self.edit_inventory()

    def terminal(self):
        key = input("> ")
        if key == "inventory":
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
            battle(0).loop()
            self.terminal()
        else:
            print("\033[31mCommand not founded, please type help for commands\033[0m")
            self.terminal()

control().terminal()
