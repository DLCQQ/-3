from tkinter import *

class Character:
    def __init__(self, race, profession, weapon, hp, damage):
        self.race = race
        self.profession = profession
        self.weapon = weapon
        self.hp = hp
        self.damage = damage

def create_character():
    race = race_var.get()
    profession = profession_var.get()
    weapon = weapon_var.get()
    
    if race == "" or profession == "" or weapon == "":
        result_label.config(text="Please select all options")
    else:
        # Define characteristics based on selected options
        if race == "Human":
            hp = 100
            damage = 10
        elif race == "Elf":
            hp = 80
            damage = 15
        elif race == "Dwarf":
            hp = 120
            damage = 8
        
        if profession == "Warrior":
            hp += 20
            damage += 5
        elif profession == "Mage":
            hp -= 10
            damage += 10
        elif profession == "Archer":
            damage += 8
        
        if weapon == "Sword":
            damage += 5
        elif weapon == "Staff":
            damage += 3
        elif weapon == "Bow":
            damage += 7
        
        new_character = Character(race, profession, weapon, hp, damage)
        
        result_label.config(text=f"Character created!\nRace: {new_character.race}\nProfession: {new_character.profession}\nWeapon: {new_character.weapon}\nHP: {new_character.hp}\nDamage: {new_character.damage}")

# Create GUI
root = Tk()
root.title("RPG Character Registration")
root.geometry("400x300")  # Set window size

race_var = StringVar()
profession_var = StringVar()
weapon_var = StringVar()

race_label = Label(root, text="Race:")
race_label.pack()
race_options = ["Human", "Elf", "Dwarf"]
race_menu = OptionMenu(root, race_var, *race_options)
race_menu.pack()

profession_label = Label(root, text="Profession:")
profession_label.pack()
profession_options = ["Warrior", "Mage", "Archer"]
profession_menu = OptionMenu(root, profession_var, *profession_options)
profession_menu.pack()

weapon_label = Label(root, text="Weapon:")
weapon_label.pack()
weapon_options = ["Sword", "Staff", "Bow"]
weapon_menu = OptionMenu(root, weapon_var, *weapon_options)
weapon_menu.pack()

register_button = Button(root, text="Create Character", command=create_character)
register_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
