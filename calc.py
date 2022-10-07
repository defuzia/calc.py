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


# while True:
#         message = input()
#         word = []
#
#         alphabets = ["abcdefghijklmnopqrstuvwxyz", "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя", "0123456789"]
#         for i in message:
#                 if i in alphabets[0]:
#                         if i == alphabets[0][-1]:
#                                 index = 0
#                         else:
#                                 index = alphabets[0].index(i) + 1
#                         word.append(alphabets[0][index])
#                 elif i in alphabets[1]:
#                         if i == alphabets[1][-1]:
#                                 index = 0
#                         else:
#                                 index = alphabets[1].index(i) + 1
#                         word.append(alphabets[1][index])
#                 elif i in alphabets[2]:
#                         if i == alphabets[2][-1]:
#                                 index = 0
#                         else:
#                                 index = alphabets[2].index(i) + 1
#                         word.append(alphabets[2][index])
#                 else:
#                         word.append(i)
#
#
#
#         res = ''
#         for i in word:
#                 res += i
#         print(res)


# while True:
#     alphabet = {"eng": "abcdefghijklmnopqrstuvwxyz",
#                 "ukr": "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя",
#                 "nums": "0123456789"
#                 }
#     encrypt = input("Enter a clear message: ").lower()
#     encrypted = ""
#     for letter in encrypt:
#         if letter in alphabet["eng"]:
#             position = alphabet["eng"].find(letter) + 1
#             if letter in alphabet["eng"][-1]:
#                 encrypted = encrypted + alphabet["eng"][0]
#             else:
#                 encrypted = encrypted + alphabet["eng"][position]
#         elif letter in alphabet["ukr"]:
#             position = alphabet["ukr"].find(letter) + 1
#             if letter in alphabet["ukr"][-1]:
#                 encrypted = encrypted + alphabet["ukr"][0]
#             else:
#                 encrypted = encrypted + alphabet["ukr"][position]
#         elif letter in alphabet["nums"]:
#             position = alphabet["nums"].find(letter) + 1
#             if letter in alphabet["nums"][-1]:
#                 encrypted = encrypted + alphabet["nums"][0]
#             else:
#                 encrypted = encrypted + alphabet["nums"][position]
#         else:
#             encrypted = encrypted + letter
#     print(encrypted)


text = input("Введіть текс: ")
mode = input("Введіть режим редагування(A/B/C): ")

edited_text = []
output = ""
for i in text.split():
    i = i.rstrip(",")
    i = i.rstrip(".")
    i = i.lower()
    if mode == "A" and len(i) > 3:
        edited_text.append(i)
        edited_text.sort()
    elif mode == "B" and len(i) > 3:
        edited_text.append(i)
    elif mode == "C" and len(i) > 3:
        edited_text.append(i)

if edited_text and mode == "A":
    edited_text = set(edited_text)
    edited_text = list(edited_text)
    edited_text.sort()
    for i in edited_text:
        output += i + "\n"
    print(output)
elif edited_text and mode == "B":
    output = {}
    for i in edited_text:
        word_counter = edited_text.count(i)
        output[i] = word_counter

    sorted_dict = sorted(output.items(), key=lambda x: x[1])
    for i, j in sorted_dict[-1:-6:-1]:
        print(i, "-", j)

elif edited_text and mode == "C":
    edited_text.sort(key=len)
    edited_text = edited_text[-1:-6:-1]

    for i in edited_text:
        output += i + "\n"

    print(output)
