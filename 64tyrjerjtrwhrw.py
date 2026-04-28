import random
class Pet:
    def __init__(self, name,health,happiness,clean,hunger ):
        self.name = name,
        self.health = health
        self.happiness = happiness
        self.clean = clean
        self.hunger = hunger
    def play(self, amount):
        self.__happiness += amount
        print("he played")
    def show_status(self):
        print(self.health,self.__happiness,self.clean, self.hunger)
    def bath(self):
        self.clean += 10
    def eat(self):
        food_tpye = input("what type of food Options apple-10 meat-100 eggs-50 vegatables -0")
        if food_tpye == "apple":
            self.hunger += 10
        if food_tpye == "meat":
            self.hunger += 100
        if food_tpye == "egg":
            self.hunger += 50
        if food_tpye == "vegatable":
            self.hunger += 0
            print("Are u tryna kill him?")
    def drop(self):
        if random.randit(1,3) == "3":
            self.__happiness -= 10
            self.clean -= 10
            self.hunger -= 10



# Petname = input("what name is ur peyt")
# user = False
# while user == False:
#     print (Petname)
#     Petname = Pet(Petname,100,50,10,10,50)
#     action = input (" waht u wanana do Options play, bath and eat ")
#     if action =="play":
#         Petname.play(10)
#         Petname.show_status()
#     if action == "bath":
#         Petname.bath()
#         Petname.show_status()
#     if action == "eat":
#         Petname.eat()
#         Petname.show_status()




Petname = input("what name is ur peyt")
pet = Pet(Petname,100,50,50,50)
X = False
Emergency = False
while X == False:
    if pet.happiness < 10:
        print("ur pet is unhappy")
        Emergency = True
    if pet.clean < 10:
        print("so dirty")
        Emergency = True
    if pet.hunger < 10:
        print("hungry")
        Emergency = True
    if Emergency == True:
        Required_Action = input (" waht u wanana do based on  the issue options play, bath and eat ")
        if Required_Action =="play":
            Petname.play(10)
            Petname.show_status()
        if Required_Action == "bath":
            Petname.bath()
            Petname.show_status()
        if Required_Action == "eat":
            Petname.eat()
            Petname.show_status()
    
