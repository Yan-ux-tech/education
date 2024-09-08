def calculate_sum(data):
    total = 0  # Для хранения общей суммы

    # Рекурсивная функция для подсчёта суммы чисел и длин строк
    def recursive_sum(element):
        nonlocal total

        # Если элемент - число, добавляем его к общей сумме
        if isinstance(element, int):
            total += element

        # Если элемент - строка, добавляем её длину
        elif isinstance(element, str):
            total += len(element)

        # Если элемент - список, кортеж или множество, проходим по всем его элементам
        elif isinstance(element, (list, tuple, set)):
            for item in element:
                recursive_sum(item)

        # Если элемент - словарь, обрабатываем и ключи, и значения
        elif isinstance(element, dict):
            for key, value in element.items():
                recursive_sum(key)  # Проверяем ключ
                recursive_sum(value)  # Проверяем значение

    recursive_sum(data)
    return total



data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_sum(data_structure)
print("Сумма всех чисел и длин строк:", result)
