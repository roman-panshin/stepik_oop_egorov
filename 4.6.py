class Doctor:

    def __init__(self, degree):
        self.degree = degree

    def can_cure(self):
        print('doc can cure')

    def can_build(self):
        print('doc can build')


class Builder:

    def __init__(self, rang):
        self.rang = rang

    def can_build(self):
        print('builder can build')


class Person(Doctor, Builder):

    def __init__(self, rang, degree):
        super().__init__(degree)
        Builder.__init__(self, rang)

        # self.rang = rang
        # self.degree = degree

    def __str__(self):
        return f"{self.rang}, {self.degree}"

    # def can_build(self):
    #     print('person said')
    #     super().can_build()
    #     Builder.can_build(self)


# print(Person.__mro__)

# s = Person(5, 'good')
# print(s)


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


class Employee(Person, Company):
    def __init__(self, name, age, company_name, location):
        super().__init__(name, age)
        Company.__init__(self, company_name, location)


emp = Employee('Jessica', 28, 'Google', 'Atlanta')
emp.display_person_info()
emp.display_company_info()
