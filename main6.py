# #Функции
# def calc():
#     num1 = int(input("ВВедите первое число "))
#     num2 = int(input("ВВедите второе число "))
#     print(num1 + num2)
# # calc()

# def hello_world():
#     print("Hello World")
# # hello_world()

# def func_while():
#     while True:
#         print("GeekTech")
# # func_while()

# def calc(num1, num2):
#     print(num1, num2)
# calc(10, 20) #K парамитрам num1, num2 передаются 10 и 20 

# numbers = [10, 20, 1, 5, 3, 44]
# print(max(numbers))

# def max(arg):
#     print("GeekTech")
# print(max(numbers))

# def print(word):
#     pass
# print("Hello World")

# def hello_user(name : str) -> str:
#     print("Здраствуйте", name)
# hello_user("Acma")
# hello_user("Asylbek")
# hello_user("Daniel")
# # hello_user(30)

# def add(num1 : int, num2 : int):
#     print(num1 + num2)

# def sub(num1 : int, num2 : int):
#     print(num1 - num2)

# def mult(num1 : int, num2 : int):
#     print(num1 * num2)

# def div(num1 : int, num2 : int):
#     print(num1 / num2)

# def main(num1 : int, num2 :int, opertor : str):
#     if opertor == "+":
#         add(num1,num2)
#     elif opertor == "-":
#         sub(num1, num2)
#     elif opertor == "*":
#         mult(num1, num2)
#     elif opertor == "/":
#         div(num1, num2)
#     else:
#         print("Error")
# main(30, 30, "+")
# main(10, 10, "*")
# # main(25, 5, "/")

# def chet_nechet(number : int = 2) -> str:
#     if number % 2 == 0:
#         print(number, "Четный")
#     else:
#         print(number, "нечетный")
# chet_nechet(222)
# chet_nechet(333)
# # chet_nechet()

# numbers = [10, 20, 33, 44, 1, 3, 2, 99, 102, 103]
# tup_numbers = (2, 3, 4, 1, 100, 33, 12, 11, 10)
# def lict_chet(lst_num : list) -> str:
#     for num in lst_num:
#         if num % 2 == 0:
#             print(num, "четный")
#         else:
#             print(num, "нечетный")
# lict_chet(numbers)
# lict_chet(tup_numbers)

# def hello():
#     return "Hello GeekTech"
# print(hello())