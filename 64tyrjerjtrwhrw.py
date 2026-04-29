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
        food_tpye = input("what type of food Options apple-10 meat-100 eggs-50 vegatables -10,  ")
        if food_tpye == "apple":
            self.hunger += 10
        elif food_tpye == "meat":
            self.hunger += 100
        elif food_tpye == "egg":
            self.hunger += 50
        elif food_tpye == "vegatables":
            self.hunger += -10
            print("Are u tryna kill him?")
        elif food_tpye == "cookie":
            self.hunger += -1000
            self.health = 0
            print("he might be deid")
    def dirty(self):
        d = input("type of play dirt, mud and rocks.")
        if d == "dirt":
            self.clean += -5
        elif d == "mud":
            self.clean += -10
        elif d == "rock":
            self.clean += -15
            self.health - 10
        elif d == "self.kill":
            self.health += -100
            self.happiness += -50
            self.clean += -50
            self.hunger += -50
        print("he is duirty")


    def injuried(self):
        if random.randint(1,3) == "3":
            print("fell down")
            self.health += -10
        elif random.randint(1,3) == "2":
            print("got bit")
            self.health += -20
        else:
            print("got attacked")
            self.health += -50



            


Petname = input("what name is ur peyt   ")
pet = Pet(Petname,100,50,50,50)
Emergency = False
while pet.health > 0:
    if random.randint(1,3) == "3":
        print("uh, ur pet got hungry isnt clean, isnt happy")
        pet.happiness += -10
        pet.clean += -10
        pet.hunger += -10
       
        if pet.hunger <= 0:
            pet.health = 0
        if pet.clean <= 0:
            pet.health = 0
        if pet.happiness <=0:
            pet.health = 0


        if pet.health == 0:
            print("pet dead")

    if pet.happiness == 10:
        print("ur pet is unhappy")
        Emergency = True
    elif pet.clean == 10:
        print("so dirty")
        Emergency = True
    elif pet.hunger == 10:
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
        pet.dirty()
    elif Regular_Action == "bath":
        pet.bath()
        
    elif Regular_Action == "eat":
        pet.eat()
    else:
        print("hahah missclickjed so u get punished")
        pet.injuried
    pet.show_status()
    
    