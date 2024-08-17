first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
#if first == second == third:
    #print(3)
#elif first == second or first == third or second == third:
    #print(2)
#elif first != second or first != third or second != third:
    #print(0)
a = [first, second, third]
b = set(a)
if len(a) == len(b):
    print(0)
else:
    print(len(a) - len(b) + 1)