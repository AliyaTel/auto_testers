# Список (list) — это упорядоченная коллекция, в которой можно хранить несколько
# значений в одной переменной. Элементы могут быть любого типа: числа, строки,
# даже другие списки.

a =  4, 8
print(type(a))

a = [ 'text', 4, 5, ]
a = list()
# mixed_list = [25, "Привет", 3.14, True, [1, 2, 3], {"name": "Алия"}, (10, 20), 'ggg']
# print(mixed_list[-1])
# mixed_list.append('text')
# print(len(mixed_list))
# mixed_list.insert(4, '888')
# mixed_list.remove("888")
# rem = mixed_list.pop()
# mixed_list[1] = 'Hello'
# print(mixed_list)
# print(rem)

ttuple = (4,)
# ttuple = (4, 8, 4, 5)
# a = tuple()
# print(ttuple.count(4))
# print(ttuple[0])
print(type(ttuple))

# sset = {} - словарь
# llist = [1, 4.4, 78, 65, 65, 1, 78, 56]
# my_sset = {25, 56, 23.4, 45}
# my_sset.add(45)
# my_sset.remove(56)
# print(25 in my_sset)
# # print(type(sset))
# sset = list(set(llist))
# print(sset)
# print(my_sset)

# my_dict = {'name': 'Tim', 'b': [12, 45]}
# my_dict['a'] = 'text'
# my_dict['num'] = 9
# print(my_dict.keys())
# my_dict.values()
# my_dict.items()
# del my_dict['a']
# print(my_dict['a'])

# Распаковка - используется для того, чтобы распределить элементы коллекции (список,
# словарь, множество, кортеж) по отдельным переменным. используется только в ситуациях,
# когда вы наверняка знаете количество элементов, содержащихся в коллекции.

# my_list = [1, 7, 8]
# my_tuple = (8, 9)
# # a = my_list[0]
# # b = my_list[1]
# # c = my_list[2]
# a, b, c = my_list
# print(a, b, c)


# Срез - Извлечение среза позволяет взять из списка определенную его часть.
my_list = [1, 7, 8, 7, 5, 4, 6, 3, 1]
print(my_list[::-2])
print(my_list[0:4:1])
print(my_list[:2])
print(my_list[5:])
print(my_list[-2:-6:-1])

# Методы строк - Со строкой можно делать многое из того, что можно делать с
# другими коллекциями, т.к. строка по сути тоже коллекция - последовательность
# символов. Больше всего функциональность строки похожа на функциональность кортежей.

str = 'My string, my string'
print(str[4])
print(len(str))
print(str.index('s'))
print('my' in str)
print(str.count('m'))
print(str.index('my'))
print(str.find('s'))
print(str[:5])
print(str.startswith('My'))
print(str.endswith('ing'))
text = 'my teXt Is So lOngEr'
print(text.capitalize())
print(text.title())
print(text.upper())
print(text.lower())

text = text.replace('my', 'you')
print(text)

text = '"admin"'
text = text.strip('"')
text = text.lstrip()
text = text.rstrip()
print(text)
