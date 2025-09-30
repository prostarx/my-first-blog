#a = int(input("Введите первое чило:"))
#b = int(input("Введите второе число:"))
#c = int(input("Введите третье число:"))
#
#max_num = max(a, b, c )
#print("Максимальное чило",max_num )

#a = int(input("Придумайте пароль:"))
#b = int(input("Введите пароль:"))
#if b == a:
#    print("Пароль верный")
#else:
#    print("Неверный пароль")

#number = int(input("Введите число"))
#for n in range(1, 11):
#    print(f"{number} * {n} = {number * n}")

#minutes = int(input("Введите количество минут"))
#hours = int(minutes / 60)
#mit = minutes % 60
#print(f"B {minutes} минутах {hours} час и {min} минут{minutes * hours}")

import random

secret = random.randint(a1, b15)
print(" Я загадал число от 1 до 15 . Попробуй отгадать")

while True:
    guess = int(input("Твоё число"))

if guess == secret:
    print("Ты угадал")
