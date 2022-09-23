# def calculate():
#     a, b, op = int(input("Введіть число а: ")), int(input("Введіть число b: ")), input("Введіть математичну операцію: ")
#
#     res = {"+": lambda x, y: x + y,
#            "-": lambda x, y: x - y,
#            "*": lambda x, y: x * y,
#            "/": lambda x, y: x / y,
#            "**": lambda x, y: x ** y}[op](a, b)
#
#     return res
#
#
# while True:
#     try:
#         print(calculate())
#     except ZeroDivisionError as ex:
#         print("""
#     ПОМИЛКА!!!
#     Ділення на нуль
#     """)


# while True:
#     a, b, op = int(input("Введіть число а: ")), int(input("Введіть число b: ")), input("Введіть математичну операцію: ")
#
#     try:
#         if op == "+":
#             res = a + b
#         elif op == "-":
#             res = a - b
#         elif op == "*":
#             res = a * b
#         elif op == "/":
#             res = a / b
#         elif op == "**":
#             res = a ** b
#         else:
#             res = "НЕВІРНА МАТЕМАТИЧНА ОПЕРАЦІЯ"
#
#         print(res)
#     except ZeroDivisionError as ex:
#         print("""
#         ПОМИЛКА!!!
#         Ділення на нуль
#         """)


# while True:
#     a, b, op = int(input("Введіть число а: ")), int(input("Введіть число b: ")), input("Введіть математичну операцію: ")
#
#     if op == '/' and b == 0:
#         print('Помилка!!!  Ділення на нуль')
#     elif op == '/':
#         print(a / b)
#     elif op == '+':
#         print(a + b)
#     elif op == '-':
#         print(a - b)
#     else:
#         print(a * b)
#





###############################################################################################################################################






while True:
        message = input()
        word = []

        alphabets = ["abcdefghijklmnopqrstuvwxyz", "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя", "0123456789"]
        for i in message:
                if i in alphabets[0]:
                        if i == alphabets[0][-1]:
                                index = 0
                        else:
                                index = alphabets[0].index(i) + 1
                        word.append(alphabets[0][index])
                elif i in alphabets[1]:
                        if i == alphabets[1][-1]:
                                index = 0
                        else:
                                index = alphabets[1].index(i) + 1
                        word.append(alphabets[1][index])
                elif i in alphabets[2]:
                        if i == alphabets[2][-1]:
                                index = 0
                        else:
                                index = alphabets[2].index(i) + 1
                        word.append(alphabets[2][index])
                else:
                        word.append(i)



        res = ''
        for i in word:
                res += i
        print(res)