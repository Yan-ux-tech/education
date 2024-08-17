my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
b = 0
# Первый цикл где мы доходим до первого отрицательного числа
first_cycle_result = []
while a < len(my_list):
    if my_list[a] < 0:
        break
    first_cycle_result.append(my_list[a])
    a += 1

# Второй цикл где мы упираемся в конец списка
second_cycle_result = []
while b < len(my_list):
    if my_list[b] > 0:
        second_cycle_result.append(my_list[b])
    b += 1

# Вывод первого цикла
print("Результат первого цикла")
for num in first_cycle_result:
    print(num)
#Вывод второго цикла
print("Результат второго цикла")
for num in second_cycle_result:
    print(num)