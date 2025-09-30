#numbers = []
#s = 0
#n = int(input("Введи количество элкементов списка"))
#for i in range(n):
#    num = int(input(f"Введите число{i + 1}:"))
#    numbers.append(num)
#print("Исходный код ", numbers)
#for l in range(len(numbers)):
#    s += numbers[l]
numbers = []
while True:
    m = int(input("вывод бесконечных чисел"))
    if m ==0:
        break
    numbers.append(m)
s = sum(numbers)
print("Сумма", s)