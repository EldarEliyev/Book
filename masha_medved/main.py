import time
import random

class Girl:
    def __init__(self, name: str, surname: str, age: int, weight: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        self.girl_hp = random.randint(50, 100)

class Bear:
    def __init__(self, name, surname, age, weight, girl: Girl):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        self.bear_hp = random.randint(100, 500)
        self.girl = girl  
    def chosen_fight_weapon(self):
        weapon_war = ["hand", "sword", "shield", "claw"]
        while True:
            chosen_war = input("Please enter your chosen (hand, sword, shield, claw): ")
            print(f"You entered: {chosen_war}")
            if chosen_war in weapon_war:
                print(f"You chose {chosen_war}")
                return chosen_war
            else:
                print("Invalid choice! Try again")

    def use_hand(self):
        self.bear_hp -= self.girl.girl_hp
        if self.bear_hp <= 0:
            return f"Bear lost. Bear Hp is: {self.bear_hp}"
        time.sleep(3)
        return f"Masha wins. Masha Hp is: {self.girl.girl_hp} And Bear Hp is: {self.bear_hp}"

    def use_claw(self):
        self.girl.girl_hp -= self.bear_hp
        if self.girl.girl_hp <= 0:
            time.sleep(2)
            return f"Masha lost. Masha Hp is: {self.girl.girl_hp}"
        else:
            time.sleep(2)
            print(f"Bear wins. Bear Hp is: {self.bear_hp}")
            time.sleep(5)
            return "Fight continues"

    def use_shield(self):
        self.girl.girl_hp -= self.bear_hp
        if self.bear_hp <= 0:
            time.sleep(1)
            return f"Bear lost: Bear Hp is: {self.bear_hp}"
        time.sleep(1)
        return f"Masha wins. Masha Hp is: {self.girl.girl_hp}"

    def use_sword(self):
        damage = self.girl.girl_hp * 0.05
        self.bear_hp -= damage
        time.sleep(4)
        print(f"Bear Hp after sword attack: {self.bear_hp}")
        if self.bear_hp <= 0:
            time.sleep(8)
            return f"Masha wins! Masha Hp is: {self.girl.girl_hp}"

    def fight(self):
        weapon = self.chosen_fight_weapon()  
        if weapon == "hand":
            print(self.use_hand())
        elif weapon == "claw":
            print(self.use_claw())
        elif weapon == "shield":
            print(self.use_shield())
        elif weapon == "sword":
            print(self.use_sword())

masha = Girl("Masha", "Natasha", 3, 3.45)
bear = Bear("Bear", "Medved", 15, 44.5, masha)

bear.fight()