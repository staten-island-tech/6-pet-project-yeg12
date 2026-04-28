import random
class Pet:
    def __init__(self, name,health,happiness,clean,hunger ):
        self.name = name,
        self.health = health
        self.happiness = happiness
        self.clean = clean
        self.hunger = hunger
    def play(self, amount):
        self.happiness += amount
        print("he played")
    def show_status(self):
        print(self.health,self.happiness,self.clean, self.hunger)
    def bath(self):
        self.clean += 10
    def eat(self):
        food_tpye = input("what type of food Options apple-10 meat-100 eggs-50 vegatables -10")
        if food_tpye == "apple":
            self.hunger += 10
        if food_tpye == "meat":
            self.hunger += 100
        if food_tpye == "egg":
            self.hunger += 50
        if food_tpye == "vegatables":
            self.hunger += -10
            print("Are u tryna kill him?")
    def died():
        if self.hunger == 0:
            self.health = 0
        if pet.hunger == -30:
            pet.health -= 40
        if pet.hunger == -50:
            pet.health -=50
        if pet.health == 0:
            print("dead")
            


Petname = input("what name is ur peyt   ")
pet = Pet(Petname,100,50,50,50)
X = False
Emergency = False
while X == False:
    if random.randint(1,3) == "3":
        pet.happiness -= 10
        pet.clean -= 10
        pet.hunger -= 10

    if pet.hunger == 0:
        pet.health = 0
    if pet.hunger == -30:
        pet.health -= 40
    if pet.hunger == -50:
        pet.health -=50
    if pet.health == 0:
        X = True

    if pet.happiness < 10:
        print("ur pet is unhappy")
        Emergency = True
    elif pet.clean < 10:
        print("so dirty")
        Emergency = True
    elif pet.hunger < 10:
        print("hungry")
        Emergency = True
    else:
        Emergency = False

    if Emergency == True:
        Required_Action = input (" waht u wanana do based on  the issue options play, bath and eat ")
        if Required_Action =="play":
            pet.play(10)
            
        elif Required_Action == "bath":
            pet.bath()
            
        elif Required_Action == "eat":
            pet.eat()
        pet.show_status()
    

    Regular_Action = input (" waht u wanana do options play, bath and eat ")
    if Regular_Action =="play":
        pet.play(10)
        
    if Regular_Action == "bath":
        pet.bath()
        
    if Regular_Action == "eat":
        pet.eat()
    pet.show_status()
   