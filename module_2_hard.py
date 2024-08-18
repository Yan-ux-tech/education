pole1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
a = 1
b = 1
ans_ = {}  # Хранение ответа
for num in pole1:
    cm = []
    while a < (num / 2):
        while b < num:
            if num % (a + b) == 0 and a != b:
                cm.append({a, b})
            b += 1
        b = 1
        a += 1
    # Удаление дубликатов списка
    for ind, e in enumerate(cm):
        for ind2, ee in enumerate(cm):
            if e == ee and ind != ind2:
                cm.pop(ind2)
    # Распаковка множества
    code = []
    for e in cm:
        code.extend(e)
    ans_.update({num: ''.join(str(el) for el in code)})
    a = 1
    b = 1
    print(f'{num} : {ans_[num]}')
