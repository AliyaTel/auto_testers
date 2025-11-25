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




