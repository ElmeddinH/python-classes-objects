#!/usr/bin/env python3
"""Day 21: Classes and Objects - Exercises Level 1, 2, 3"""


# ============ LEVEL 1 ============

# 1. Python has the type() function to check the data type of certain data/variable
print(type(10))
print(type(3.14))
print(type(1 + 3j))
print(type('Asabeneh'))
print(type([1, 2, 3]))
print(type({'name': 'Asabeneh'}))
print(type({9.8, 3.14, 2.7}))
print(type((9.8, 3.14, 2.7)))


# 2. Create a Person class with the following properties and methods
class Person:
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh',
                 age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return (f'{self.firstname} {self.lastname} is {self.age} years old. '
                f'He lives in {self.city}, {self.country}.')

    def add_skill(self, skill):
        self.skills.append(skill)


p1 = Person()
print(p1.person_info())

p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
print(p1.skills)


# ============ LEVEL 2 ============

# 3. Create a Student class that inherits from Person
class Student(Person):
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh',
                 age=250, country='Finland', city='Helsinki',
                 gender='male'):
        super().__init__(firstname, lastname, age, country, city)
        self.gender = gender

    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return (f'{self.firstname} {self.lastname} is {self.age} years old. '
                f'{gender} lives in {self.city}, {self.country}.')


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki', 'male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


# ============ LEVEL 3 ============

# 4. Override the person_info method and check the gender
# Already done in Student class above with gender check

# 5. Create an Animal class
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


# Testing Animal classes
dog = Dog('Rex', 5, 'Brown', 'German Shepherd')
print(dog.animal_info())
print(dog.bark())
print(f'Breed: {dog.breed}')

cat = Cat('Whiskers', 3, 'White', True)
print(cat.animal_info())
print(cat.meow())
print(f'Indoor: {cat.indoor}')

print("\n--- All exercises completed! ---")
