#name = input("Введите ваше имя")
#print("привет,",name)
#print(660+1000000000000000000000000)
#print("Hello")
#if 5 < 7:
    #print("Hello")
#'''
#Вывод на консоль
#сообщение Hello world
#'''
#print("Hello World")
#name ="Tom"
#print(name)
#isMarried = False
#print(isMarried)    # False
from django.template.defaultfilters import yesno

#isAlive = True
#print(isAlive)      # True
#age = 21
#print("Возраст:", age)     # Возраст: 21

#count = 15
#print("Количество:", count) # Количество: 15
#a = 0b11
#b = 0b1011
#c = 0b100001
#print(a)        # 3 в десятичной системе
#print(b)        # 11 в десятичной системе
#print(c)        # 33 в десятичной системе

#a = 0o7
#b = 0o11
#c = 0o17
#print(a)    # 7 в десятичной системе
#print(b)    # 9 в десятичной системе
#print(c)    # 15 в десятичной системе

#a = 0x0A
#b = 0xFF
#c = 0xA1
#print(a)    # 10 в десятичной системе
#print(b)    # 255 в десятичной системе
#print(c)    # 161 в десятичной системе

#height = 1.68
#pi = 3.14
#weight = 68.
#print(height)   # 1.68
#print(pi)       # 3.14
#print(weight)   # 68.0

#x = 3.9e3
#print(x)  # 3900.0

#x = 3.9e-3
#print(x)  # 0.0039
#complexNumber = 1+2j
#print(complexNumber)   # (1+2j)
#message = "Hello World!"
#print(message)  # Hello World!

#name = 'Tom'
#print(name)  # Tom
#'''
#Это комментарий
#'''
#text = '''Laudate omnes gentes laudate
#Magnificat in secula
#Et anima mea laudate
#Magnificat in secula
#'''
#print(text)
#text = "Message:\n\"Hello World\""
#print(text)
#userName = "Tom"
#userAge = 37
#user = f"name: {userName}  age: {userAge}"
#print(user)   # name: Tom  age: 37
#userId = "abc"  # тип str
#print(userId)

#userId = 234  # тип int
#print(userId)
#userId = "abc"  # тип str
#print(type(userId))  # <class 'str'>

#userId = 234  # тип int
#print(type(userId))  # <class 'int'>
#name = input("Введите свое имя: ")
#print(f"Ваше имя: {name}")
#name = input("Your name: ")
#age = input("Your age: ")
#print(f"Name: {name}  Age: {age}")
#number = 10
#number += 5
#print(number)   #15

#number -= 3
#print(number)   #12

#number *= 4
#print(number)   #48
#first_number = 2.0001
#second_number = 5
#third_number = first_number / second_number
#print(third_number) # 0.40002000000000004
#print(2.0001 + 0.1)  # 2.1001000000000003
#first_number = 2.0001
#second_number = 0.1
#third_number = first_number + second_number
#print(round(third_number))  # 2
#first_number = 2.0001
#second_number = 0.1
#third_number = first_number + second_number
#print(round(third_number, 4))  # 2.1001
# округление до целого числа
#print(round(2.49))  # 2 - округление до ближайшего целого 2
#print(round(2.51))  # 3
#print(round(2.5))   # 2 - ближайшее четное
#print(round(3.5))   # 4 - ближайшее четное
# округление до двух знаков после запятой
#print(round(2.554, 2))      # 2.55
#print(round(2.5551, 2))      # 2.56
#print(round(2.554999, 2))   # 2.55
#print(round(2.499, 2))      # 2.5
# округление до двух знаков после запятой
#print(round(2.545, 2))  # 2.54
#print(round(2.555, 2))  # 2.56 - округление до четного
#print(round(2.565, 2))  # 2.56
#print(round(2.575, 2))  # 2.58

#print(round(2.655, 2))  # 2.65 - округление не до четного
#print(round(2.665, 2))  # 2.67
#print(round(2.675, 2))  # 2.67
#a = 5
#b = 6
#result = 5 == 6  # сохраняем результат операции в переменную
#print(result)  # False - 5 не равно 6
#print(a != b)  # True
#print(a > b)  # False - 5 меньше 6
#print(a < b)  # True

#bool1 = True
#bool2 = False
#print(bool1 == bool2)  # False - bool1 не равно bool2

#x and y

#age = 22
#weight = 58
#result = age > 21 and weight == 58
#print(result) # true

#result = 4 and "w"
#print(result)

#result = 0 and "w"
#print(result)

#x or y

#age = 22
#isMarried = False
#result = age > 21 or isMarried
#print(result)

#result = 4 or "w"
#print(result)

#result = 0 or "w"
#print(result)

#age = 22
#isMarried = False
#print(not age > 21)
#print( not isMarried)
#print(not 4)
#print(not 0)

#message = "hello world"
#hello = "world"
#print(hello in message)

#gold = "gold"
#print(gold in message)

#message = "hello world!"
#hello = "hello"
#print(hello not in message)

#gold = "gold"
#print(gold not in message)
