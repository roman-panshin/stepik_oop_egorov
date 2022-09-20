# exceptions

def first():
    print('start first')
    try:
        second()
    except ZeroDivisionError:
        print('exception')
    print('end first')


def second():
    print('start second')
    third()
    print('end second')


def third():
    print('start third')
    1 / 0
    print('end third')


print('hello1')
first()
