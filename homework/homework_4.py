name = input("Введите ваше имя: ")
age = int(input("Введите ваш год рождения: "))
city = input("Введите ваш город: ")
mailing = input("Согласие на рассылку: ")
if mailing == "yes": mailing = True
elif mailing == "no": mailing = False
print (f"name = {name} \nage = {age} \ncity = {city} \nmailing = {mailing}")