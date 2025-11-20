import random

# Funstions - это самые основные программные структуры в языке Python, позволяющие многократное использование
# программного кода и уменьшающие его избыточность. Так же позволяют разбить сложную систему на достаточно
# простые и легко управляемые части. Они могут принимать аргументы и возвращать результаты выполнени

# DRY - don’t repeat yourself

a = 1
b = 5
c = 4
d = 7
y = 5

main_number = 47
if y == 0:
    print(a + main_number)
if y == 0:
    print(b + main_number)
if y == 0:
    print(c + main_number)
if y == 0:
    print(d + main_number)


def calc(numb):
    if y == 0:
        print(numb + main_number)


calc(a)
calc(b)
calc(c)
calc(d)
calc(y)

# return используется внутри функций, чтобы вернуть результат работы функции наружу. Иначе
# говоря, когда функция что-то вычисляет, return позволяет получить этот результат и использовать
# его дальше. return print возвращает None

def calc1(numb):
    if y == 0:
        return numb
    else:
        result = numb + main_number
        return result


number = calc1(56)
print(number)

#параметры и аргументы
def p_words(first, second, third, fourth, fifth):
    print(f'The first word is {first}, second word is {second}, {third}, {fourth}, {fifth}')


#использование позиционных аргументов
p_words('one', 'two', 'three', 'four', 'five')

#использование именованных аргументов
p_words(fifth='one', third='two', fourth='four', first='three', second='five')


# использование дефолтных аргументов
def power(number, degree = 2):
    return number ** degree


print(power(2))
print(power(2, 3))


#после передачи именованных аргументов, все остальные тоже должны быть именованными
def example(e, f, g, ff='one', gg='two'):
    print(e, f, g, ff, gg)


example(2, 3, 6, ff='three')


# *args, **kwargs
def sum_all(*args):
    # print(args)
    results = 0
    for i in args:
        results += i
    return results


print(sum_all(1, 2, 3, 4, 5, 56))


def price_list(**kwargs):
    print(kwargs)
    for title, price in kwargs.items():
        print(f'Product {title} price is {price}')


price_list(iphone=2500, laptop=150, samsung=2000, monitor=1000)

# модули

print(random.random())

# декораторы


def my_decorator(func):
    def wrapper():
        print("Функция скоро запустится")
        func()
        print('Функция завершена')
    return wrapper


@my_decorator
def say_hello():
    print("Привет!")


say_hello()

