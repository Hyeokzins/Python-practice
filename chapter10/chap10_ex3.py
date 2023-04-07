class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError('Subclasses must implement abstract method')


class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof!'
    
animals=[Cat('missy'),Cat('jerry'),Dog('tom')]

for animal in animals:
    print(animal.name +':'+animal.talk())