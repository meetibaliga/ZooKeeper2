from animal import Animal
from strategyp import *

class Feline(Animal):

    def getFamily(self):
        return 'Feline'

    # Strategy Pattern: Felines roam by referencing strategy RoamNormalStrategy()
    def roam(self):
        return RoamNormalStrategy().roam()


    def eat(self):
        return " is eating like a Feline."

class Pachyderm(Animal):

    def getFamily(self):
        return "Pachderm"

    # Startegy Pattern: Pachyderms roam by referencing strategy RoamNormalStrategy()
    def roam(self):
        return RoamNormalStrategy().roam()

    def eat(self):
        return " is eating like a Pachyderm."

class Canine(Animal):

    def getFamily(self):
        return "Canine"

    # Startegy Pattern: Canines roam by referencing strategy RoamNormalStrategy()
    def roam(self):
        return RoamNormalStrategy().roam()

    def wakeUp(self):
        return " is waking up like a Canine."

    def makeNoise(self):
        return " is making noise like a Canine."

class Fish(Animal):

    def getFamily(self):
        return "Fish"

    def makeNoise(self):
        return " is making noise by jumpling like a Fish."

    # Strategy Patterm: Fish roam by referencing strategy RoamBySwimStrategy()
    def roam(self):
        return RoamBySwimStrategy().roam()

class Bird(Animal):

    def getFamily(self):
        return "Bird"

    # Strategy Pattern: Birds roam by referencing strategy RoamByFlyStrategy()
    def roam(self):
        return RoamByFlyStrategy().roam()

    def sleep(self):
        return " is sleeping like a Bird."
