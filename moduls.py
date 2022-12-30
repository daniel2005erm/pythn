#1 импортировать сам модуль
# import main7
# print(main7.get_time())
# print(main7.hello())

# #2 импортировать отдельные определения из модуля
# from main7 import get_time, hello
# print(get_time())
# print(hello())

#3 Импортировать всё содержимое модуля сразу
# from main7 import *
# print(get_time())
# print(hello())
# print(it)

from main7 import numbers, chet

def chet_nechet(num : list) -> list:
    for i in num:
        if i % 2 == 0:
            chet.append(i)
    return chet
# print(chet_nechet(numbers))