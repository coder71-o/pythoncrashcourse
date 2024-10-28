class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"{self.name}: Greetings!")

    def instigate(self, opponent_name):
        print(f"{self.name}: I am here to fight you {opponent_name}!")
    
    def attack(self, opponent):
        print(f"{self.name} is attacking {opponent.name}!")
        
        print(f"{self.name} does {self.strength} damage!")
        opponent.health = opponent.health - self.strength
        print(f"{opponent.name} has {opponent.health} health remaining.")
        

character_1 = Character("Bob", 50, 20)
character_2 = Character("Lilith", 100, 15)

# print(character_1.name, character_1.health)
# print(character_2.name, character_2.health)

character_1.greet()
character_2.instigate(character_1.name)
print(character_2.health)
character_1.attack(character_2)
