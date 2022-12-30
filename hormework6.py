
# def shorter(phrase):
#     phrase_dict = phrase.split()
#     for i in range(len(phrase_dict)):
#         print(phrase_dict[i] [0], end = '')
# shorter('Кыргызстан Республика')

# prinimaet = {}
# def user(ltr):
#     umenshaet_spl = ltr.lower().split(" ")
#     for name in umenshaet_spl:
#         prinimaet[name] = umenshaet_spl.count(name)
# user("Money, money, money, it's always sunny, in the richmen's word")
# print(prinimaet)

# def izogramma(word):
#     izogramma_1 = list(word)
#     izogramma_2 = set(word)
#     if len(izogramma_1) == len(izogramma_2):
#         return True
#     return False
# print(izogramma("truee"))

# def numbers(num):
#     return int(str(num)[::-1])
# print(numbers(27))

# def chatbot():
#     while True:
#         text = input("Введите что то: ")
#         if text.find("?")>=0:
#             print("Конечно!")
#         elif text.find("!")>=0:
#             print("Успокойся")
#         elif text == "":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("Ну и что")
# chatbot()