#Циклы for, while
# for i in range(1, 101, 2):
#     print(i)

# names = ["Kurmanbek", "Daniel", "Askhat", "Nursultan"]
# print(names)
# for g in names:
#     print(g)
#     if g == "Askhat":
        # print("Аскат есть")

# numbers = [1, 10, 11, 12, 44, 33, 100, 101, 120, 102]
# for num in numbers:
#     if num % 2 == 0:
#      print(num, "четный")
#     else:
#         print(num, "нечет")

# # name = "Kurmanbek"
# for n in name:
#     if n == "a":
#      print("Буква а  есть в имени")

# numbers = "100" 
# for num in numbers:
#     print(num)

# cities_tup = ("Osh", "Bishkek", "Talas", "Tokmok")
# for city in cities_tup:
#     print(city)

# cars = {"BMW", "MERSEDES", "TESLA", "HONDA"}
# for i in cars:
#     print(i)

# student = {"name" : "Daniel", "age" : 18, "language" : "Python"}
# for key, value in student.items():
#     # print(key, value)
#     if key == "language" and value == "Python":
#         print("Питонист найден")
#     else:
#         print("Else")

# numbers = []
# for n in range(1, 1001):
#     numbers.append(n)
# print(numbers)

# for i in range(1, 11):
#     print(i)
#     if i == 6:
#         print("STOP")
#         # break
#      continue

# numbers = [10, 20, 30, 40, 50, "Hello"]
# for i,n in enumerate(numbers):
#     print(i, n)

# num1 = 10
# num2 = 20
# while num1 < num2:
#     print(num1)
#     # num1 = num1 + 1
#     num1 += 1

# import random

# n = 0 
# random_numbers = random.randint(1, 100)
# print(random_numbers)
# while True:
#     n += 1
#     print(n)
#     if n == random_numbers:
#         print("Найден")
#         break

# import time

# process = 0 
# while True:
#     print(str(process) + "% HACK")
#     process += 10
#     time.sleep(3)
#     if process == 100:
#         print("HACKED")
#         break