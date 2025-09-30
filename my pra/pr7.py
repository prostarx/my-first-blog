text = input("Введите предложение")
print(text.replace(" ","_"))
print("Количество пробелов =", text.count(" "))
text = input("Введите предложение:")

#word = "Привет"
#for i in range(len(word), -1, -1):
#     print(word[:i])

#word = "Привет"
#for i in range(len(word) + 1):
#     print(word[i:])

numbers = []
n = int(input("Сколько чисел будет в списке: "))
for i in range(n):
     num = int(input(f"Введите число {i+1}:"))
     numbers.append(num)
     result = sum(numbers)
     average = result / len(numbers)
     maximum = max(numbers)
     minimum = min(numbers)
print("Список чисел ", numbers)
print("Cумма чисел ", result)
print("Сведение Арифметическое ", average)
print("Максимум ", maximum)

