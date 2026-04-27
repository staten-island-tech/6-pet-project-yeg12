class Pet:
    def __init__(self, name,health,happiness, attack,clean,hunger ):
        self.name = name,
        self.health = health
        self.__happiness = happiness
        self.attack = attack
        self.clean = clean
        self.hunger = hunger
    def play(self, amount):
        self.__happiness += amount
        print("he played")

    def show_status(self):
        if self.__happiness >= 80:
            print( " very happy")
        elif self.__happiness >= 50:
            print ("mid ")
        else:
            print ("very very very very very sad ")
    def attack (self,attacked):
        self.health -= attacked
        print(self.health)
    def clean(self):
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



class Prey:
    def __init__  (self,name, health):
        self.name = name
        self.health = health

    def attacked(self,damage):
        self.attack = damage
        self.health -= damage
        if self.health == 0:
            print("prey is dead")

    def status(self):
        if self.health == 0:
            print("dead",self.health)
        if self.health >= 1:
            print("You know I'm still standing better than I ever did Looking like a true survivor, feeling like a little kid I'm still standing after all this time ",self.health)
user = False
while user == False:
    Petname = input("what name is ur peyt")
    print (Petname)
    Petname = Pet(Petname,100,50,10,10,50)
    action = input (" waht u wanana do Options play, clean and eat ")
    if action =="play":
        Petname.play(10)
        Petname.show_status()


