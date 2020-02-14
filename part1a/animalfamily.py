from animal import Animal

class Feline(Animal):

    def getFamily(self):
        return 'Feline'

    def roam(self):
        return "roaming like Feline."

    def eat(self):
        return "eating like Feline."

class Pachyderm(Animal):

    def getFamily(self):
        return " Pachderm"

    def eat(self):
        return "eating like Pachyderm."

class Canine(Animal):

    def getFamily(self):
        return " Canine"

    def wakeUp(self):
        return "Waking like Canine."

    def makeNoise(self):
        return "making noise like Canine."
