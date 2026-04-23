class Pet:
    def __init__(self, name,health,happiness, attack ):
        self.name = name
        self.__happiness = happiness
        self.health = health
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
        if self.health == 0:
            print("hahahhah, hwo did he died, lmao, this so so sad, ur such a smart guy")
class prey:
    def _init_  (self,name, health, defence):
        self.name = name
        self.health = health
        self.defence = defence
    def attacked(self,damage):
        self.attackattack = damage
        defence -= damage
        if defence == 0:
            health -= defence
        if health == 0:
            print("prey is dead")
    
rex = Pet("rex",100,50,10)
trex = prey("big T",10000,100)
trex.attacked(10)
