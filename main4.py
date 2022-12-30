#Множества set, frozenset
# a = [1, 3, 4, 5]
# b = [3, 4, 5, 6]
# print(list(set(a + b)))

# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 2}
# print(numbers)
# # print(numbers[0]) #нельзя в set выводить по индексу
# print(numbers[0:2]) #Set не поддерживает срезы

# names = {"Askhat", "Kurmanbek", "Daniel", "Asylbek"}
# print(names)
# names.add("Nursultan") #Добавляем Nursultan в set множество
# print(names)
# names.remove("Askhat") #Удаляем Askhat из мнижества
# print(names)
# names.pop() #Удаляем случайное значение 
# # print(names)
# # names.update("Kurmanbek") #Добавляет Kurmanbek и делит по буквам
# print(names)
# names.clear() #Очищаем set
# print(names)

# lst = []
# print(type(lst))
# hello = ""
# print(type(hello))
# st = {}
# print(type(st))

# lst = [10, 4.0, False, "Geek", [1, 2, 3], {1, 2, 3, 3}]
# print(lst)
# st = {1, 1.0, True, "1"}
# numbers = {10, 5, 20, 100, 1, 2, 3}
# print(st)
# print(numbers)
# frzn = frozenset([1, 2, 3, 4, 5, 6, 6])
# print(frzn)
# # frzn.add(10)
# print(frzn)

# #Tuple - Кортеж
# numbers = (1, 10, 11, 2, 3, 4, 4, 5, 6)
# print(numbers)
# tup = (1, 1.0, True, "Hello", [1, 2, 3], {1, 2, 2}, (10, 20))
# print(tup)
# print(tup.count(20))
# print(tup.index(1))
# print(tup[2])
# print(tup[0:3])

# cars = ("BMW", "Mersedes", "Ferrari")
# print(cars)
# lst_cars = list(cars)
# print(lst_cars)
# lst_cars.append("Tesla")
# print(lst_cars)
# cars = tuple(lst_cars)
# print(cars)

# tup = (10,)
# print(type(tup))

# student = {"student" : "Askhat", "age" : 18} #Создаем словарь student
# print(student)
# print(len(student)) #Выводим длину словаря student
# print(student['age']) #По ключу age выводим значение с ловаря student
# student.setdefault('language', 'Python')#Добавляем с словарь новый ключ и значение
# print(student)
# student.pop('age')#Удаляем по кл
# print(student)
# student['language'] = 'JavaScript'
# print(student)
# student['place_study'] = 'GeekTech'
# print(student)
# print(student.keys())
# print(student.values())

# сontact = {'Askhat' : "0778909091"}
# while True:
#     command = input("1 - получить все контакты, 2 - добавить контакт, 3 - удалить контакт, 4 - обновить контакт: ")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         add_name = input("ВВедите имя: ")
#         add_number = input("ВВедите номер")
#         if add_name not in contact.keys():
#             contact.setdefault(add_name, add_number)
#             print("Успешно добавлено")
#         else:
#             print("Такой контакт уже существует")
#     elif command == "3":
#       if delete_contact = input("Кого удалить")
#         contact.pop(delete_contact)
#         print("Успешно удалено")
#     else:
#         print("Такого контакта нету")
        