# ЗАДАНИЕ ПО ТЕМЕ "Генераторы"

# Вывод всех подпоследовательностей строки в следующем порядке:
# сначала подстроки, содержащие 1 символ, затем - 2 символа и т.д.
# [0:1], [1:2], [2:3], ..., [0:2], [1:3], ..., [0:3], ...
def all_variants1(text):
    for j in range(len(text)):
        for k in range(len(text) - j):
            yield text[k:k + j + 1]


# Вывод всех подпоследовательностей строки в следующем порядке:
# сначала подстроки, начинающиеся с 1-го символа, затем - со 2-го символа и т.д.
# [0:1], [0:2], [0:3], ..., [1:2], [1:3], ..., [2:3], ...
def all_variants2(text):
    for j in range(len(text)):
        for k in range(j, len(text)):
            yield text[j:k + 1]


a1 = all_variants1('abc')

for i in a1:
    print(i)
print()

a2 = all_variants2('abc')

for i in a2:
    print(i)
