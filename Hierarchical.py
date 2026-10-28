class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Cat(Animal):
    def meow(self):
        print("Meowing")


d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()