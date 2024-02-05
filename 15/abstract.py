from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def say(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def jump(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meaow"

    def run(self):
        return 'Cat runs'

    def jump(self):
        return 'Cat jumps'


class Dog(Animal):
    def say(self):
        return "Woof"

    def run(self):
        return "Dog runs"

    def jump(self):
        return "Dog jumps"


dog = Dog()
cat = Cat()
print(cat.say())
print(cat.run())
print(cat.jump())
print(dog.say())
print(dog.run())
print(dog.jump())