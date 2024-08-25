def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 2)
print_params(b=25, c=[1, 2, 3])

values_list = [96, 'Uga', False]
values_dict = {'a': 45, 'b': 'Строчичка', 'c': 2.5}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [25, 'string']
print_params(*values_list_2, 42)
