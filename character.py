import random
class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.is_alive = True

    def greet(self):
        print(f"{self.name}: Greetings!")

    def instigate(self, opponent_name):
        print(f"{self.name}: I am here to fight you {opponent_name}!")
    
    def attack(self, opponent):
        damage = self.damage()
        print(f"{self.name} is attacking {opponent.name}!")
        print(f"{self.name} does {damage} damage!")
        opponent.health = opponent.health - damage
        if (opponent.health < 0):
            opponent.is_alive = False
            print(f"{opponent.name} has died!")
        else:
            print(f"{opponent.name} has {opponent.health} health remaining.")

    def damage(self):
        return self.strength + random.randrange(0,int((self.strength)/2)) - self.strength/4
        

character_1 = Character("Bob", 50, 20)
character_2 = Character("Lilith", 100, 15)

# print(character_1.name, character_1.health)
# print(character_2.name, character_2.health)

character_1.greet()
character_2.instigate(character_1.name)

while character_1.health > 0 and character_2.health > 0:
    if(random.randrange(0,2)) == 0:
        character_1.attack(character_2)
        if character_2.is_alive:
            character_2.attack(character_1)
    
    else:
        character_2.attack(character_1)
        if character_1.is_alive:
            character_1.attack(character_2)
    
