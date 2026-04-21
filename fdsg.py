# class Calculator():
#     def add(x, y):
#         print(x + y)
#         return x + y

#     def add_many(numbers):
#         print(sum(numbers))
#         return sum(numbers)

#     def subtract(numbers):
#         return numbers

# Calculator.add(10, 6)


# class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.money = money
#         self.inventory = inventory

#     def buy(self, item):
#         self.inventory.append(item)
#         print(self.inventory)
# bob = Hero ("bob",0.01,["a slipper"] )
# bob.buy({"title": "Sword", "atk": 34})
# print(bob.__dict__)

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  
#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print(f"{self.owner} has ${self.__balance}")

class Hero:
    def __init__(self, name,balance,inventory):
        self.name = name
        self.balance = balance 
        self.inventory = inventory
    def buy(self, item, price):
        self.inventory.append(item)
        self.balance -= price
        print(self.inventory)
    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):

        print(f"{self.owner} has ${self.__balance}")
class pet:
    def _init

bob = Hero ("bob",100,["slipper"] )
bob.buy({"title": "Sword", "atk": 34}, 10)
print(bob.__dict__)

