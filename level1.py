#!/usr/bin/env python3

print(type(10))
print(type(3.14))
print(type(1 + 3j))
print(type('Asabeneh'))
print(type([1, 2, 3]))
print(type({'name': 'Asabeneh'}))
print(type({9.8, 3.14, 2.7}))
print(type((9.8, 3.14, 2.7)))


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
