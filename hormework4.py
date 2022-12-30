
# it_company = ('Google', 'Amazon', 'Microsoft')
# tup_cities = tuple(it_company)
# print(tup_cities)
# lct_citise = list(tup_cities)
# lct_citise.append('Tesia')
# tup_cities = tuple(lct_citise)
# print(tup_cities)

# it_company = ('Coogle', 'Microsoft', 'Tesia')
# tup_citise = tuple(it_company)
# print(tup_citise)
# lct_citise = list(tup_citise)
# lct_citise.append('Amazon')
# tup_citise = tuple(lct_citise)
# print(tup_citise)

# it_company = ('google', 'amazon', 'microsoft')
# tup_company = tuple(it_company)
# print(tup_company)
# lst_company =  list(tup_company)
# print(lst_company)
# lst_company[0] = 'apple'
# tup_company = tuple(lst_company)
# print(tup_company)

# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'python', 'overview')
# print(text_tuple.count("python")) #1

# name_1 = {'a': 300, 'b': 400}
# name_2 = {'c': 500, 'd':600}
# name_1.update(name_2)
# print(name_1)

# numbers = numbers = {'num_1' : 1, 'num_2' : 2,'num_3' : 3, 'num_100' : 100}
# numbers['num_1'] = 1 * 5
# numbers['num_2'] = 2 * 5
# numbers['num_3'] = 3 * 5
# numbers['num_100'] = 100 * 5
# print(numbers)

# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] = 17 * 2
# print(student)

# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] = 16
# print(student)
 
# student = {'name' : 'Askhat', 'age' : 17}
# student.pop("age")
# print(student)

# student = {'name' : 'Askhat'}
# student.setdefault('address', 'Западный Анар')
# print(student)

# parol = {}
# while True:
#     frist_parol = input("введите пароль: ")
#     posledov_1 = frist_parol.find("123")
#     posledov_2 = frist_parol.find("qwe")
#     if len(frist_parol) > 7:
#         if posledov_1 < 0 and posledov_2 < 0:
#             parol.setdefault('first_p', frist_parol)
#             proverka_paroly = input("введите повторный пароль:")
#             if parol['first_p'] == proverka_paroly:
#                 print("ok")
#             else:
#                 print("различаються")
#         else:
#             print("простой пароль")
#     else:
#         print("короткий пароль")
#     print(parol)

# contact = {"MCHS" : 112}
# while True:
#     command = input("1 - посмотреть все контакты, 2 - добавить контакт, 3 - удалить контакт, 4 - обновить контакт: ")
#     if command == "1":
#         for name, number in contact.items():
#             print(name, number)
#     elif command == "2":
#         add_name = input("введите имя которую вы хотите добавить: ")
#         add_number = input("введите номер которую вы хотите добавить: ")
#         contact.setdefault(add_name, add_number)
#         print("контакт добавлен")
#     elif command == "3":
#         delete_contact = input("введите имя коротую хотим удалить: ")
#         if delete_contact in contact.keys():
#             del contact[delete_contact]
#             print("контакт удален") 
#         else:
#             print("не наден")
#     elif command == "4":
#         update_name = input("введите контакт который хотите обновить: ")
#         if update_name in contact.keys():
#             print("хотите обновить текуший номер")
#             update_number = input("введите номер: ")
#             contact[update_name] = update_number
#             print("контакт обновлен")
#         else:
#             print("контакт не найден хотите добавить новый контакт")
#             add_number = input("введите номер: ")
#             contact.setdefault(update_name, add_number)
#             print("контакт добавлен")
#     else:
#         print("выбраная вами команда не сушествует")
#         break

# it_company = ('Google', 'Amazon', 'Microsoft')
# print(it_company[0:3:2])
