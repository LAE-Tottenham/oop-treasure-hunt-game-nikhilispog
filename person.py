from random import *
class Person:
    def __init__(self,name,hp,defence,dmg):
        self.name = name
        self.hp = hp
        self.defence = defence
        self.dmg = dmg
class Player(Person):
    def __init__(self,name,hp,defence,dmg):
        super().__init__(name,hp,defence,dmg)
        self.gold = 0
        self.bag = [None]

    def interact(self,place,game):
        if place == 0: 
            print("Nothing is here")
            game.loadNothing()
        if place == 1:
            game.loadItem()
        if place == 2:
            game.loadNPC()
        if place == 3:
            game.loadEnemy()

    def attack(self,map,enemy):
        weaponDMG = 0
        for item in self.bag():
            if isinstance(item, Weapon): # have to make separate item class
                if item.damage>weaponDMG:
                    weaponDMG = item.damage
        hit = (self.dmg+randint(1,30)-enemy.defence+weaponDMG)
        enemy.hp-= hit
        print("You dealt", str(hit), "damage to the enemy")
        if enemy.hp<=0:
            map.deleteTile()
            print("You vanquished", enemy.name)
        else:
            hit = (enemy.dmg+(randint(1,20))-self.defence)
            self.hp -= hit
            print("The enemy dealt", str(hit), "damage to you")
        if self.hp<= 0:
            self.die()
    def die(self,game):
        print("Everything goes dark... and you die.")
        game.dead = True 
    def takeItem(self,item):
        if len(self.bag)<5:
            self.bag.append(item)
            print("Item was added to your bag")
        else:
            print("Not enough space, you cannot take this item")
class Enemy(Person):
    pass
class NPC():
    def __init__(self,name,item,dialogue):
        self.name = name
        self.item = item
        self.dialogue = dialogue
    def speak(self):
        print(self.dialogue)
    def giveItem(self,player):
        print(f"As a token of my gratitude, I offer you {self.item.name}")
        choice = input("Would you like to take it? (yes/no)")
        if choice == "yes":
            player.takeItem(self.item)
            print("You thank", self.name, "for their kindness")
        else:
            print("You refuse their offer")
