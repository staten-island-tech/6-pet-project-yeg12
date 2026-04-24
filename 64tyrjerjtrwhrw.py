class Pet:
    def __init__(self, name,health,happiness, attack ):
        self.name = name
        self.health = health
        self.__happiness = happiness
        self.attack = attack

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
    def restart (self, health):
        if self.__happiness == 0:
            print("hahahhah, hwo did he died, lmao, this so so sad, ur such a smart guy")
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
    
nuhun = Pet("pet",100,50,10)
nuhun.show_status()
litlle=Prey("name",12)
litlle.attacked()
litlle.status()

