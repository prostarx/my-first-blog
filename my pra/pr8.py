numbers = []
n = int(input("Введи количество чисел списка:"))
for i in range(n):
    num =int(input(f"Введите число {i+1}: "))
    numbers.append(num)
print("исход, список: ", numbers)
numbers = [num for num in numbers if num % 2 !=0]
result = sum(numbers)
average = result / len(numbers)
maximum = max(numbers)
minimum = min(numbers)
negative = sum(1 for num in numbers if num <0)
print("Ваш список " , numbers)
print("Сумма чисел ", result)
print("Среднее арифметическое: ", average)
print("Максимум: ", maximum)
print("Минимум: ", maximum)
print("Отриц, числа:", negative)
numbers = [num for num in numbers if num % 2 != 0]
print("Удаление четных чисел ", numbers)
for i in range(len(numbers)):