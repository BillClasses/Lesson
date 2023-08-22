import time
import random

class Player():
    # Class Attributes
    active = True
    norm_attack = "NORMAL ATTACK!!!"
    
    # Instance Attributes
    def __init__(self, name ,type_class, skill_class, level, health, atk, speed):
        self.name = name
        self.type_class = type_class
        self.skill_class = skill_class
        self.level = level
        self.health = health
        self.atk = atk
        self.speed = speed
        self.storage = storage
        
    # Status Board
    def show_status_board(self):
        print("\n \n")
        print("====================Player Status====================")
        print("Name: {}".format(self.name))
        print("Level: {}".format(self.level))
        print("Skill: {}".format(self.skill_class))
        print("Health: {}".format(self.health))
        print("Attack Damage: {}".format(self.atk))
        print("Speed: {}".format(self.speed))
        print("\n \n")
    
    #  Change class
    def change_class(self, type_class_change):
        self.type_class = type_class_change
    
    # Change name
    def change_name(self, name_change):
        self.name = name_change
    
    # Infinity Damage 
    def Infite_DMG(self):
        self.atk = 99999999999999999999999999999
    # Attack
    def attack(self, name):
        damage = random.randint(self.atk - 10, self.atk + 10)
        print("Attack: {}".format(damage))
        
class Enemy():
    def __init__(self, type, health, attack, speed, skill):
        self.type = type
        self.health = health
        self.attack = attack
        self.speed = speed
        self.skill = skill
    
    # Status Board
    def show_status_board(self):
        print("\n \n")
        print("====================Enemy Status====================")
        print("Name: {}".format(self.type))
        print("Health: {}".format(self.health))
        print("Skill: {}".format(self.skill))
        print("Attack Damage: {}".format(self.attack))
        print("Speed: {}".format(self.speed))
        print("\n \n")
    
    def receive_dmg(self, damaged):
        self.health -= damaged
        print("Player Deal: {}".format(damaged))
        if damaged > damaged + 5: critical = True
        if (critical): print("Critical Damaged!!!")
        
    def attack(self, attack_dmg):
        return random.randint(attack_dmg - 10, attack_dmg + 10)

    def skill(self, skill_dmg):
        print("Skill Damage({}): {}".format(self.skill, skill_dmg))
        

def attack_system(Player, Enemy):
    print("Deal Damage")
    
items = ["Sword", "Shield", "Gun", "Shotgun", "AK47", "M4A1", "AR15", "Desert Eagle"]
storage = []
name = input("Enter Player Name: ")
class_type = input("Pick Your Class (Warrior, Warlock, Archer, Tanker): ")
new_player = Player("Bill", "Warrior", "Brave_Player", 999, 100, 0, 2.4)
new_player.show_status_board()
new_orc = Enemy("Orge", 3000, 300, 1, "Orc Scream")
new_orc.show_status_board()



