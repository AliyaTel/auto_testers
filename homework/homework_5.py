# secretNumber = 7
# guess = None
# while guess != secretNumber:
#      guess = int(input("Введите число:  "))
#      if guess != secretNumber:
#          print("Попробуй еще ")
# print("поздравляем, верно!")
#
# text = "Мама мыла раму, папа читал газету, а кот спал на диване"
# words = text.split()
# count_a = 0
# i = 0
# while i < len(words):
#     word = words[i]
#     if "а" in word.lower():
#         count_a += 1
#     i += 1
# print(f"количество слов с буквой а: {count_a}")
from operator import length_hint, contains


def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet():
    return ("hello world")
print(greet())

def has_a(word):
    return "а" in word.lower()
print(has_a("Яблоко"))
print(has_a("Груша"))
print(has_a("Ананас"))
print(has_a("Лайм"))
print(has_a("Малина"))

def has_a(word):
    return "а" in word.lower()

def word_length(word):
    return len(word)

def analyze_sentence(sentence):
    for ch in ",.!?;:":
        sentence = sentence.replace(ch, "")
        words = sentence.split(" ")

    for word in words:
        length = word_length(word)
        contains_a = has_a(word)
        print(f"Слово: {word:<10} | Длина: {length:2} | Есть 'а': {contains_a}")

text = "Мама мыла раму, папа читал газету, а кот спал на диване"
analyze_sentence(text)


class Animal:
    def __init__(self, name, owner, age):
        self.name = name
        self.owner = owner
        self.age = age

    def voice(self):
        print(gav)

    def eat(self):
        print(food)


class Cat(Animal):

    def __init__(self, name, owner, age, mouse):
        super().__init__(name, owner, age)
        self.mouse = mouse

    def voice(self):
        print("meu")

    def eat(self):
        print("cookies")


class Dog(Animal):

    def __init__(self, name, owner, age, colors):
        super().__init__(name, owner, age)
        self.colors = colors

    def voice(self):
        print("gav")

    def eat(self):
        print("bread")


cat_1 = Cat("Barsik", "Andrey", 2, "yes")
cat_1.eat()
cat_1.voice()
print(cat_1.name)
print(cat_1.owner)
print(cat_1.age)
print(cat_1.mouse)


dog_2 = Dog("Sharik", "Viktor", 4, "white")
dog_2.voice()
dog_2.eat()
print(dog_2.name)
print(dog_2.owner)
print(dog_2.age)
print(dog_2.colors)

file = open("home_data1.txt", "r")
data = file.readlines()
for line in data:
    line = line.strip() #не обяз строка (просто есть уже)
    print(line)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название {self.title}, Автор {self.author}, Год {self.year}"


class Fiction(Book):
    def get_info(self):
        return f"Название {self.title}, Автор {self.author}, Год {self.year}"


class NonFiction(Book):
    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Жанр: Non-Fiction"


book1 = Fiction("1984", "Джордж Оруэлл", 1949)
book2 = Fiction("Мастер и Маргарита", "М. Булгаков", 1967)
book3 = NonFiction("Краткая история времени", "Стивен Хокинг", 1988)
book4 = NonFiction("Самая большая тайна", "Дэвид Айк", 1999)

books = [book1, book2, book3, book4]

for book in books:
    print(book.get_info())


