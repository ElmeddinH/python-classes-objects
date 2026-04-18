#!/usr/bin/env python3


class Animal:
    def __init__(self, name, age, color, legs=4):
        self.name = name
        self.age = age
        self.color = color
        self.legs = legs

    def animal_info(self):
        return (f'{self.name} is {self.age} years old. '
                f'It is {self.color} and has {self.legs} legs.')


class Dog(Animal):
    def __init__(self, name, age, color, breed, legs=4):
        super().__init__(name, age, color, legs)
        self.breed = breed

    def bark(self):
        return f'{self.name} says: Woof Woof!'


class Cat(Animal):
    def __init__(self, name, age, color, indoor=True, legs=4):
        super().__init__(name, age, color, legs)
        self.indoor = indoor

    def meow(self):
        return f'{self.name} says: Meow!'


dog = Dog('Rex', 5, 'Brown', 'German Shepherd')
print(dog.animal_info())
print(dog.bark())
print(f'Breed: {dog.breed}')

cat = Cat('Whiskers', 3, 'White', True)
print(cat.animal_info())
print(cat.meow())
print(f'Indoor: {cat.indoor}')
