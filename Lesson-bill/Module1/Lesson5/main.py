

name = "Tui"
__name = ""

def print_name_tui():
    __name = "Tui tui"
    print(__name)

def print_name_noibo():
    global __name
    print(__name)
    
print_name_tui()
print_name_noibo()


class Vehicle():
    def __init__(self, type):
        self.type = type
    
    def description(self):
        print("Tôi là phương thiện giao thông! {}".format(self.type))
        
class Car(Vehicle):
    pass


create_vehicle = Vehicle("Vehicle")
create_car = Car("Car")

create_vehicle.description()
create_car.description()

class RPG_System():
    def __init__(self, health, armor, critical_dmg, atk, defend, class_type, storage):
        self.health = health
        self.armor = armor
        self.critical_dmg = critical_dmg
        self.atk = atk
        self.defend = defend
        self.storage = storage
        self.class_type = class_type
        self.storage = storage
    
    def status_board(self):
        __health = self.health
        __armor = self.armor
        __critical_dmg = self.critical_dmg
        __atk = self.atk
        __defend = self.defend
        __class_type = self.class_type
        
        print("\n\n\n")
        print("=================Status=================")
        print("Class | {}".format(__class_type))
        print("Health | {}".format(__health))
        print("Armor | {}".format(__armor))
        print("Critical Dmg | {}".format(__critical_dmg))
        print("Atk | {}".format(__atk))
        print("Defend | {}".format(__defend))
        
        
    def storage_manager(self):
        __storage = self.storage
        
        print("\n")
        print("================Storage==================")
        for i in __storage:
            print("|{}|".format(i))
            
Storage_Player = ["Swords", "Rings", "Armors", "Medicine", "Health Potion"]
RPG_Player = RPG_System(300, 500, 900, 700, 1000, "Warrior", Storage_Player)
RPG_Player.status_board()
RPG_Player.storage_manager()
        