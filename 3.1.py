# magic methods ___str__ and __repr__
import random


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'the object Lion - {self.name}'

    def __str__(self):
        return f'Lion - {self.name} {"zloy" if random.randint(0, 1) == 0 else "dobriy"}'


q = Lion('Bob')
s = Lion('simba')

print(str(q))
print(str(s))
