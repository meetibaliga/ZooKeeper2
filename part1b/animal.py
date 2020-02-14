from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name

    def sleep(self):
        return "Sleeping."

    def wakeUp(self):
        return "Waking up."

    def eat(self):
        return "Eating."

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    @abstractmethod
    def roam(self):
        pass

    @abstractmethod
    def makeNoise(self):
        pass

    @abstractmethod
    def getFamily(self):
        pass

    @abstractmethod
    def getType(self):
        pass
