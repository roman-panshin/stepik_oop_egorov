class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def deposit(self, summa):
        self.__balance += summa

    def payment(self, summa):
        if summa > self.__balance:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        self.__balance -= summa
        return True


class Cart:
    def __int__(self, user):
        self.user = user
        self.goods = {}
        self.__total = 0

    def add(self, product, count=1):
        self.goods[product.name] = count
        self.__total += product.price * count

    def remove(self, product, count=1):
        if self.goods[product.name] < count:
            self.__total -= product.price * self.goods[product.name]
            self.goods[product.name] = 0
        else:
            self.goods[product.name] -= count
            self.__total -= product.price * count

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        for item in self.goods:
            print(f'{self.}')
        {Имя
        товара} {Цена
        товара} {Количество
        товара} {Сумма}

        print(f'---Total: {self.total}--- ')






# billy = User('billy@rambler.ru')
# print(billy) # Пользователь billy@rambler.ru, баланс - 0
# billy.deposit(100)
# billy.deposit(300)
# print(billy) # Пользователь billy@rambler.ru, баланс - 400
# billy.payment(500) # Не хватает средств на балансе. Пополните счет
# billy.payment(150)
# print(billy) # Пользователь billy@rambler.ru, баланс - 250
