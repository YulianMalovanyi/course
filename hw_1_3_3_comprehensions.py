# -*- coding: utf-8 -*-
"""hw_1.3.3 Comprehensions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-SQlzs9OTVDPUqYOlQRbUIC6kWh43p1z

#Домашнє завдання до теми "Comprehensions в Python"

Для наступних завдань у нас є наступний список:
"""

numbers = [42, 51, 29, 2, 13, 44, 80, 66, 16]

"""1. Використовуючи цикл `for` cтворіть новий список `numbers_squared`, де кожен елемент списку `numbers` є домноженим на 2.

Нагадаю, що фактично коли ми з допомогою циклу отримуємо новий список, то ми спочатку створюємо пустий список, а потім додаємо в нього новий елемент на кожній ітерації.

Новий елемент буде в даному випадку результатом домножання чергового елемента вихідного списку `numbers` на 2.
"""

numbers_squared = [number * 2 for number in numbers]

print(numbers_squared)

"""Очікуваний результат: `[84, 102, 58, 4, 26, 88, 160, 132, 32]`

2. Використовуючи `list comprehension` cтворіть новий список `numbers_squared_lh`, де кожен елемент списку `numbers` є домноженим 2.
Так, операція, яку ми викнуємо над кожним елементом вихідного списку, та сама, що і в попередньому завданні, але інший спосіб отримання результату.
"""

numbers_squared_lh = [number * 2 for number in numbers]
print(numbers_squared_lh)

"""3. У нас вже є знайдене середнє значення за списком - воно визначене в змінній `numbers_mean`.

  Використовуючи цикл, створіть новий список `numbers_gt_mean`, який порівнює кожен елемент з цим середнім значенням за списком за наступним правилом: "якщо цей елемент спиcку `numbers` є більшим за `numbers_mean`, то запишемо 1, інакше 0". Виведіть новий список на екран.
"""

numbers_mean = 38.11

numbers_gt_mean = []

for number in numbers:
    if number > numbers_mean:
        numbers_gt_mean.append(1)
    else:
        numbers_gt_mean.append(0)

print(numbers_gt_mean)

"""Очікуваний результат: `[1, 1, 0, 0, 0, 1, 1, 1, 0]`

4. Отримайте список за тим самим правилом, що в завданні 3, тільки тепер з list comprehension. Результат запишіть у змінну `numbers_gt_mean_lc`
"""

numbers_gt_mean_lc = [1 if number > numbers_mean else 0 for number in numbers]
print(numbers_gt_mean_lc)

"""5. Заданий список `long`. З допомогою циклу створіть словник `n_repeats`, який містить інформацію "скільки разів повторюється кожен унікальний елемент списку `long`".
Наприклад:
```
long = [1, 1, 2, 2, 3]
# тоді `n_repeats` містить {1: 2, 2: 2, 3: 1}
```

Аби для кожного унікального елементу знайти, скільки разів він повторюється, виористайте метод списку `list.count(<елемент>)`.
Виведіть `n_repeats` на екран.

**Підказки**:
1. Для початку може бути зручно отримати набір унікальних елементів списку.
2. Порядок ключів в словнику не має значення! Тобто ключі в словнику не обовʼязково мають бути в тому ж порядку, як наведено в прикладі результату. Але кількості зустрічань для кожного елемента мають співпадати з наведеними.
"""

long = [75, 39, 95, 1, 91, 43, 97, 24, 86, 75, 92, 91, 15, 15, 75, 95, 54, 29, 55, 98]

n_repeats = {}
unique_elements = set(long)

for element in unique_elements:
    n_repeats[element] = long.count(element)

print(n_repeats)

"""Очікуваний результат:
```
{1: 1, 97: 1, 98: 1, 39: 1, 75: 3, 43: 1, 15: 2, 55: 1, 86: 1, 54: 1, 24: 1, 91: 2, 92: 1, 29: 1, 95: 2}

```

6. Виконайте ту саму операцію, що і в попередньому заваднні, але використовуючи `dict comprehension`. Результат запишіть у змінну `n_repeats_dh` та результат виведіть на екран.
"""

n_repeats_dh = {element: long.count(element) for element in set(long)}
print(n_repeats_dh)

"""7. Знайдіть три найменші **унікальні** елементи в списку `long` та виведіть їх на екран."""

unique_elements = set(long)
sorted_unique_elements = sorted(unique_elements)
three_smallest_elements = sorted_unique_elements[:3]
print(three_smallest_elements)

"""Очікувана відповідь: [1, 15, 24]"""