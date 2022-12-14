class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# ---

class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values) == 0:
            print("Empty Stack")
        else:
            return self.values.pop()

    def peek(self):
        if len(self.values) == 0:
            print("Empty Stack")
        else:
            return self.values[len(self.values) - 1]

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)


# ---

class Worker:
    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        print(f"Worker {self.name}; passport-{self.passport}")


persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]

worker_objects = []

for person in persons:
    worker_objects.append(Worker(*person))

for worker in worker_objects:
    Worker.get_info(worker)


# ---

class CustomLabel:
    def __init__(self, text, **kwargs):
        self.text = text
        self.config(**kwargs)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


# ---

class Battery:

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(self.battery_size)


class Rule:

    def __init__(self, rule_size=50):
        self.rule_size = rule_size

    def describe_rule(self):
        print(self.rule_size)


class Trunc:

    def __init__(self, trunc_size=50):
        self.trunc_size = trunc_size

    def describe_rule(self):
        print(self.trunc_size)


class Car:
    def __init__(self, name='volvo cars'):
        self.name = name
        self.trunc = Trunc()
        self.rule = Rule()
        self.battery = Battery()

    def describe_car(self):
        print(self.name)


# ---

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Person: {self.name}, {self.age}")


class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f"Company: {self.company_name}, {self.location}")


class Employee:
    def __init__(self, name, age, company_name, location):
        self.personal_data = Person(name, age)
        self.work = Company(company_name, location)
