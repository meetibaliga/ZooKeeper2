class Zookeeper:

    def wakeAnimals(self, animal_list):
        for animal in animal_list:
            print(animal.getName() + ' who is a' + animal.getType() + ' belonging to' + animal.getFamily() + ' is '+ animal.wakeUp())

    def feedAnimals(self, animal_list):
        for animal in animal_list:
            print(animal.getName() + ' who is a' + animal.getType() + ' belonging to' + animal.getFamily() + ' is '+ animal.eat())

    def rollCallAnimals(self, animal_list):
        for animal in animal_list:
            print(animal.getName() + ' who is a' + animal.getType() + ' belonging to' + animal.getFamily() + ' is ' + animal.makeNoise())

    def exerciseAnimals(self, animal_list):
        for animal in animal_list:
            print(animal.getName() + ' who is a' + animal.getType() + ' belonging to' + animal.getFamily() + ' is ' + animal.roam())

    def shutDownZoo(self, animal_list):
        for animal in animal_list:
            print(animal.getName() + ' who is a' + animal.getType() + ' belonging to' + animal.getFamily() + ' is ' + animal.sleep())
