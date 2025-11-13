#name = input("Введите ваше имя: ")
#age = int(input("Введите ваш год рождения: "))
#city = input("Введите ваш город: ")
#mailing = input("Согласие на рассылку: ")
#if mailing == "yes": mailing = True
#elif mailing == "no": mailing = False
#print (f"name = {name} \nage = {age} \ncity = {city} \nmailing = {mailing}")

#friend = {"name": "Kate", "age": int(30), "hobbies": {"footbol", "basket", "tennis", "dance"}, "favorite_colors": ["blue", "red", "pink", "black", "white"] }
#print(friend["name"],)
#print(friend["age"],)
#print (len(friend["hobbies"]),)
#print (len(friend["favorite_colors"]),)
#print (friend["favorite_colors"])

fio = input("Введите ваши данные, в формате: имя, возраст, город")
print(fio)

parts = fio.split(", ")
print(parts)

name, age, city = parts
print(name)
print(age)
print(city)

Name_2 = name[:2]
print(Name_2)

age_2 = int(age[:2])
print(type(age_2))

city_2 = city.capitalize()
print(city_2)
print(f"Привет, {name}! Тебе {age} лет, Ты из города {city}")
