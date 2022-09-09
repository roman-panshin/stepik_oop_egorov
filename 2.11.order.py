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
    def __init__(self, user):
        self.user = user
        self.goods = {}
        self.__total = 0

    def add(self, product, count=1):
        if product not in self.goods:
            self.goods[product] = 0
        self.goods[product] += count
        self.__total += product.price * count

    def remove(self, product, count=1):
        if self.goods[product] <= count:
            self.__total -= product.price * self.goods[product]
            del self.goods[product]
        else:
            self.goods[product] -= count
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
        result = []
        for item in self.goods:
            result.append(f'{item.name} {item.price} {self.goods[item]} {self.goods[item] * item.price}')
        print(*sorted(result), sep='\n')
        print(f'---Total: {self.total}---')


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20


# billy = User('billy@rambler.ru')
# print(billy) # Пользователь billy@rambler.ru, баланс - 0
# billy.deposit(100)
# billy.deposit(300)
# print(billy) # Пользователь billy@rambler.ru, баланс - 400
# billy.payment(500) # Не хватает средств на балансе. Пополните счет
# billy.payment(150)
# print(billy) # Пользователь billy@rambler.ru, баланс - 250
