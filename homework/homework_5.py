secretNumber = 7
guess = None
while guess != secretNumber:
     guess = int(input("Введите число:  "))
     if guess != secretNumber:
         print("Попробуй еще ")
print("поздравляем, верно!")

text = "Мама мыла раму, папа читал газету, а кот спал на диване"
words = text.split()
count_a = 0
i = 0
while i < len(words):
    word = words[i]
    if "а" in word.lower():
        count_a += 1
    i += 1
print(f"количество слов с буквой а: {count_a}")