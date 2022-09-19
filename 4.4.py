# extending

class Person:

    def combo(self):
        if hasattr(self, 'sleep'):
            self.sleep()


class Doctor(Person):
    age = 25

    def sleep(self):
        print('doc can sleep')


p = Person()
d = Doctor()

p.combo()
d.combo()
