class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        self.in_trash = False
        print(f'Файл {self.name} восстановлен из корзины')

    def remove(self):
        self.is_deleted = True
        print(f'Файл {self.name} был удален')

    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
            return

        if self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
            return

        print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
            return

        if self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
            return

        print(f'Записали значение {content} в файл {self.name}')


class Trash:
    content = []

    @staticmethod
    def add(file):
        if not isinstance(file, File):
            print('В корзину добавлять можно только файл')
        else:
            Trash.content.append(file)
            file.in_trash = True

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for file in Trash.content:
            file.remove()
        Trash.content = []
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for file in Trash.content:
            file.restore_from_trash()
        Trash.content = []
        print('Корзина пуста')




f1 = File('puppies.jpg')
f2 = File('cat.jpg')
passwords = File('pass.txt')

f1.read() # Прочитали все содержимое файла puppies.jpg
Trash.add(f1)
f1.read() # ErrorReadFileTrashed(puppies.jpg)

Trash.add(f2)
Trash.add(passwords)
Trash.clear() # после этой команды вывод должен быть таким
'''
Очищаем корзину
Файл puppies.jpg был удален
Файл cat.jpg был удален
Файл pass.txt был удален
Корзина пуста
'''

f1.read() # ErrorReadFileTrashed(puppies.jpg)

# f1 = File('puppies.jpg')
# print(f1.__dict__)  # {'name': 'puppies.jpg', 'in_trash': False, 'is_deleted': False}
# f1.read()  # Прочитали все содержимое файла puppies.jpg
# f1.remove()  # Файл puppies.jpg был удален
# f1.read()  # ErrorReadFileDeleted(puppies.jpg)
#
# f2 = File('cat.jpg')
# f2.write('hello')  # Записали значение hello в файл cat.jpg
# f2.remove()  # Файл cat.jpg был удален
# f2.write('world')  # ErrorWriteFileDeleted(cat.jpg)
