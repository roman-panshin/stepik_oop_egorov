# magic method __call__
from time import perf_counter


class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'call object {self.counter} times, len {self.length}, summa {self.summa}', self)

    def average(self):
        return self.summa / self.length


#
# s = Counter()
# s(1)
# s(2)
# s(3)
# s(3, 4, 5, 6, 6, 6, 6)
# s(4)
# s()


class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f"call function {self.fn.__name__}")
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f"function time {finish - start}")
        print(result)
        return result


@Timer  # decoration
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# fact = Timer(fact)  # one time decoration
# fact(7)

# fib = Timer(fib)  # all decoration with recursion calls
# fib(8)

# Timer(fib)(10)  # only call decoration


class Addition:
    def __call__(self, *args, **kwargs):
        summa = 0
        for i in args:
            if isinstance(i, (int, float)):
                summa += i
        print(f"Сумма переданных значений = {summa}")
        return summa


# add = Addition()
#
# add(10, 20) # печатает "Сумма переданных значений = 30"
# add(1, 2, 3.4) # печатает "Сумма переданных значений = 6.4"
# add(1, 2, 'hello', [1, 2], 3) # печатает "Сумма переданных значений = 6"


'''
Где можно использовать метод __call__ 
Реализация метода __call__ нужна, когда мы хотим, чтобы экземпляры класса вели себя как функции.
А поскольку метод __call__ делает экземпляр вызываемым, мы можем использовать его в качестве декоратора.
'''


class Storage:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Подключение к хранилищу")
        self.func()
        print("Отключение от хранилища")


@Storage
def upload_file():
    print("Загрузка файла....")


@Timer
def calculate():
    for i in range(10000000):
        2 ** 100


calculate()
