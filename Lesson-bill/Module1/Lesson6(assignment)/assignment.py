# tao 1 class Circle

# với attribute
    # radius:float instance attribute - private
    # color:str instance attribute
    # pi:float class attribute

# với method
    # get_perimeter() → float
    # change_radius(new_radius)
    # show_radius()
# tạo 4 object với radius và color khác nhau goi get_perimeter() goi change_radius() goi show radius()

# override init method với 2 arguments : radius và color viết method get_area() cho class Cirlce_v2 thay đổi radius = 10 rồi gọi lại method get area ()
import random


class Circle:
    # Class attribute
    pi = 3.14159265359

    def __init__(self, radius, color):
        # Private instance attribute
        self.__radius = radius
        self.color = color

    def get_perimeter(self):
        return 2 * Circle.pi * self.__radius

    def change_radius(self, new_radius):
        self.__radius = new_radius

    def show_radius(self):
        return self.__radius

class Circle_v2(Circle):
    def __init__(self, radius, color):
        super().__init__(radius, color)

    def get_area(self):
        # Overriding the method to calculate area
        return Circle.pi * (self.show_radius() ** 2)

# Tạo 4 đối tượng Circle với bán kính và màu sắc khác nhau
circle1 = Circle(5.0, "Red")
circle2 = Circle(7.0, "Blue")
circle3 = Circle(3.0, "Green")
circle4 = Circle(8.0, "Yellow")

# Gọi phương thức get_perimeter() cho các đối tượng Circle
print("Circle 1 Perimeter:", circle1.get_perimeter())
print("Circle 2 Perimeter:", circle2.get_perimeter())
print("Circle 3 Perimeter:", circle3.get_perimeter())
print("Circle 4 Perimeter:", circle4.get_perimeter())

# Gọi phương thức change_radius() và show_radius() cho đối tượng Circle
circle1.change_radius(6.0)
print("Circle 1 New Radius:", circle1.show_radius())

# Tạo một đối tượng Circle_v2 với bán kính 10 và màu sắc "Purple"
circle_v2 = Circle_v2(10.0, "Purple")

# Gọi phương thức get_area() cho đối tượng Circle_v2
print("Circle_v2 Area:", circle_v2.get_area())

class enemy:
    healing_mana = 30
    damage_test = 20
    def __init__(self, hp, mana, dame, speed, defense):
        self.hp = hp
        self.dame = dame
        self.mana = mana
        self.speed = speed
        self.defense = defense
    
    def attack(self):
        print("Quái vật đã gây ra {} damage!".format(self.dame))
    
    def healing(self):
        self.hp += enemy.healing_mana
        enemy.reduce_mana(self)
        print("Quái vật đã hồi {} hp!".format(enemy.healing_mana))
    
    def defended(self):
        self.hp -= (enemy.damage_test - self.defense)
        print("Quái vật đã phòng thủ {} damage!".format(self.defense))
        
    def skill(self):
        print("Quái vật đã gây ra {} skill damage!".format(self.dame * random.randint(2, 4)))

    def reduce_hp(self):
        self.hp -= enemy.damage_test
        print("Quái vật đã bị trừ {} hp".format(enemy.damage_test))
        
    def reduce_mana(self):
        self.mana = enemy.healing_mana
        print("Quái vật đã bị giảm mana đi {} mana".format(enemy.healing_mana))
        
class Orc(enemy):
    def init(self, hp, mana, dame, speed, defense):
        super().init(self, hp, mana, dame, speed, defense)
    
    def skill(self):
        print("Orc đã gây ra {} skill damage!".format(self.dame * random.randint(2, 4)))
        

orc = Orc(300, 500, 100, 0, 10)
orc.attack()
orc.healing()
orc.defended()
orc.reduce_hp()
orc.reduce_mana()
orc.skill()
