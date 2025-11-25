import json
# Классы в Python — это способ создавать свои собственные типы данных, объединяя данные (атрибуты)
# и логику (методы) в одном месте. Если упрощённо: класс — это как чертёж, а объект — это предмет,
# который построен по чертежу.

class Group:
    human = True

    def __init__(self, title, pupils_count, group_leader):
        self.title = title
        self.pupils_count = pupils_count
        self.group_leader = group_leader

    def study(self):
        print('sit down and read')

    def move(self):
        print('move')


class PrimaryGroup(Group):
    max_age = 11
    min_age = 6

    def move(self):
        print('run')


class HighGroup(PrimaryGroup):
    max_age = 18
    min_age = 14

    def __init__(self, title, pupils_count, group_leader, prom):
        super().__init__(title, pupils_count, group_leader)
        self.prom = prom

    def move(self):
        print('Go slowly')


first_a = Group('4А', 30, "Anna Ivanovna")
print(first_a.title)
print(first_a.group_leader)
print(first_a.pupils_count)
first_a.move()


second_b = HighGroup('11B', 15, "Sergei Petrov", 2025)
print(second_b.title)
print(second_b.group_leader)
print(second_b.pupils_count)
print(second_b.max_age)
print(second_b.human)
second_b.study()
second_b.move()

three_d = PrimaryGroup('1B', 40, "Dmitryi Petrov")
three_d.move()
# объект класса = представитель класса = экземпляр класса

four_a = HighGroup('10B', 10, "Almaz Petrov", 2026)
print(four_a.prom)

#🧱 Основные термины

#1. **Класс**

# Шаблон, чертёж.
# Например: «Человек», «Кошка», «Машина».
# 2. **Объект**
# Конкретный экземпляр класса.
# Например: класс «Кошка», объект — «Мурка».
# 3. **Атрибуты**
# Переменные внутри объекта (его свойства).
# Например: имя, возраст, цвет.
# 4. **Методы**
# Функции внутри класса, которые что-то делают.
# Например: мяукнуть, бежать, есть.


# ООП — это **объектно-ориентированное программирование**.
# Его идея: объединять данные и функции, которые с этими данными работают, в одну сущность — объект

def read_file(filename):
    file_data = open(filename, 'r')
    data = file_data.read()
    data = json.loads(data)
    file_data.close()
    return data["Country"]
    # return data


data1 = read_file('data1.txt')
data2 = read_file('data2.txt')

print(data1)
print(data2)

file = open('hello.txt')
data = file.readlines()

for line in data:
    print(line.strip())


