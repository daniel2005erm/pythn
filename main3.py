# it = "GeekTech" #Индексы
     #01234567
# print(it[0])
# print(it[4])
# print(it[3])
# print(it[4] + it[5] + it[6] + it[7])
# print(it[0:8]) #срезы

#List - Списки
# cars = [1, "1", True, 19.9]
# print(type(cars))

# name1 = "Kurmanbek"
# name2 = "Askhat"
# name3 = "Daniel"
# print(name1)
# names = ["Kurmanbek", "Askhat", "Daniel"]
# print(names)
# names.append("Asylbek") #добавление в конец списка
# print(names)
# names.remove("Kurmanbek") #Удаление из писка по значению
# print(names)
# names.pop(0) #Удаление из списка по ирдексу
# print(names)
# names.insert(0, "Askhat") #Добавление в список по индексу
# print(names)
# names[0] = "Asko" #Обновление значение в списке
# print(names)
# cities = ["Bishkek", "Osh", "Tokmok", "Naryn"]
# print(cities[0:2])
# print(cities[::-1])
# cities.sort()
# print(cities)
# cities.reverse()
# print(cities)

# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# # del numbers[0:3:2]
# # print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(numbers.count(70))
# print(numbers.index(80))

# contacts = ["Askhat"]
# name = input("ВВедите имя ").title
# if name in contacts:
#     print(name, "найден")
# else:
#     print(name, "не найден")

# contacts = ["Askhat"]
# while True:
#     command = input("1-посмотреть контакт, 2 - добавить в контакт, 3 - удалить контакт, 4 - обновить контаект: ")
#     if command =="1":
#         print(contacts)
#     elif command == "2":
#         add_contact = input("Кого хотите добавить?: ").title()
#         contacts.append(add_contact)
#         print("удачно добавлен")
#     elif command == "3":
#         remove_contact = input("Кого удалить?: ").title()
#         if remove_contact in contacts:
#          contacts.remove(remove_contact)
#          print("Успешно удален")
#         else:
#          print("Контакт не найден")
#     elif command == "4":
#         update_contact = input("кого хотите обновить?: ")
#         if update_contact in contacts:
#             new_contact = input("новое имя: ")
#             contacts[contacts.index(update_contact)] = new_contact
#             print("Успешно обновлено")
#         else:
#             print("Не найден")