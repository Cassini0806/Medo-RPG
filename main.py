from assets.npcs import *

def attack_mob(mob):
    mob["hp"] -= player["atk"]

def name_gender():
    print("Select your attributes, please.")
    player["name"] = input("Name: ")
    player["gender"] = input("Gender [m/f]: ")

spawn_mob(6)
show_mobs()

select_mob = monsters[0]

#print("Selected Mob: ", select_mob)
#attack_mob(select_mob)
if select_mob["hp"] == 0 or select_mob["hp"] <= 0:
        monsters.remove(select_mob)
        print("Mob Killed")
else:
    print("Attacked Mob: ", select_mob)

