# Class method vs Static Method

class Example:
    def hello():
        print('hello')  # for class only

    def instance_hello(self):
        print(f'hello {self}')  # for instance only

    @staticmethod
    def static_hello():
        print('static hello')  # for class and for instance

    @classmethod
    def class_hello(cls):
        print(f'class hello {cls}')  #


# Example.static_hello()
# p = Example()
# p.static_hello()

# Example.class_hello()
# p = Example()
# p.class_hello()
#
# print(p.__class__)


# ---

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f'Робот {self.name} был создан')
        Robot.population += 1

    def destroy(self):
        print(f'Робот {self.name} был уничтожен')
        Robot.population -= 1

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @classmethod
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось')


