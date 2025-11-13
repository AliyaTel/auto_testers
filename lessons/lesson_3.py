languages = ['Python', 'Java', 'Ruby']
# languages = ','.join(languages)
print('Student knows these languages: ', ', '.join(languages))

a = "one"
b = "two"

#string format
my_text = "First word is {1}, second word is {0}"
print(my_text.format(a, b))

# f-string
my_text = f"First word is {a}, second word is {b}"
print(my_text)

# Conditions - условия

# user_input = int(input('Введите число: '))


# if user_input == 1:
#     print('One')
# elif user_input == 2:
#     print('Two')
# elif user_input == 3:
#     print('Three')
# else:
#     print('Many')


# Loops - Циклы for и while

# names = ['James', 'Tom', 'John', 'Bob', 'Jim', 'Bill']
#
# for name in names:
#     name = name.replace('i', '7')
#     if name.startswith('J'):
#         print('Mr.', end='')
#     print(name)


# persons = {'John': 132, 'Tom': 167, 'James': 234}
#
# for person in persons.keys():
#     print(person)
#
# for person in persons.values():
#     print(person)
#
# for a, b in persons.items():
#     print(f'{a}: {b}')

# Распечатать все слова, в которых есть буква "о" и выбросить из текста, текст в конце распечатать
# text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris'
# words = text.split()
# fin_words = []
#
# for word in words:
#     if 'o' in word:
#         print(word)
#     else:
#         fin_words.append(word)
#
# print(' '.join(fin_words))

# While - это цикл, который повторяет блок кода, пока выполняется определённое условие.
# Иначе говоря, цикл идёт до тех пор, пока условие истинно.

# i = 0
#
# while i < 5:
#     print('Hello')
#     i += 1

# while True:
#     user_input = input('Enter something: ')
#     if user_input == 'exit':
#         break
#     elif user_input == 'skip':
#         continue
#     elif len(user_input) > 10:
#         print('long')
#     else:
#         print('ok')






