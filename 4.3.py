# overriding


class Person:
    name = 'vasyan'

    def __init__(self, name='gogi'):
        print('init person')
        self.name = name

    def breathe(self):
        print('person can breathe')

    def walk(self):
        print('person can walk')

    def combo(self):
        self.walk()
        self.breathe()


class Doctor(Person):
    name = 'crazy_doctor'

    def breathe(self):
        print('doctor can breathe')


p = Person('armen')
d = Doctor()

print(p.name, d.name)

d.combo()
