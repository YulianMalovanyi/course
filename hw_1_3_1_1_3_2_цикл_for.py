# -*- coding: utf-8 -*-
"""hw_1.3.1-1.3.2 Цикл for.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f9gWAT3GWcyOIROt2ZGGp0fl1EQhd6Ui

#Домашнє завдання до теми "Цикл for"

0. Розігрів. Напишіть цикл, який виводить на екран числа від 1 до 10 включно.
"""

for i in range(1, 11):
  print(i, end = " ")

"""**Початок покладено!**

1. Задайте список `numbers`, який містить значення від 0 до 9 включно. Використовуючи цикл `for`, обчисліть суму елементів в створеному списку та виведіть фінальну суму на екран.
"""

summ = 0
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers:
  summ += i
print(summ)

"""2. Використовуючи цикл  `for` виведіть для кожного елементу списку `numbers`,який ми створили в завданні 1, чи цей елемент дорівнює 5. Тобто після виконання циклу на екрані має бути 10 bool значень."""

for i in numbers:
  if i == 5:
    print(True)
  else:
    print(False)

"""3. Використовуючи цикл  `for` для кожного елементу списку `numbers`, який ми створили в завданні 1, виявіть, чи цей елемент ділиться на 2 без остачі, та запишіть результат у новий список `numbers_divisible_by_2`.

Увага! Виконання завдання відрізняється від попереднього тим, що тепер ми результат обчислення на кожній ітерації записуємо у новий список. До того ж ми тут виконуємо іншу математичну операцію.

Виведіть фільнальний список `numbers_divisible_by_2` на екран.
"""

numbers_divisible_by_2 = []
for i in numbers:
  if i % 5 == 0:
    numbers_divisible_by_2.append(True)
  else:
    numbers_divisible_by_2.append(False)
print( numbers_divisible_by_2)

"""Очікуваний результат: `[True, False, True, False, True, False, True, False, True, False]`

4. Задано два списки в клітинці нижче - `a` і `b`. Створіть цикл, результатом якого буде список `result`, що містить елементи типу bool і який фактично каже,
"чи на цьому індексі елементи наших двох списків співпадають". Приклад:
```
a = [1, 2, 3, 6]
b = [1, 7, 3, 6]
# ми виконали поелементне порівняння двох списків і отримали новий список result
# result містить наступний результат -> [True, False, True, True]
```
В кінці виведіть вміст result на екран.

<details>
<summary>Підказка</summary>

Аби порівняти елементи в циклі - треба створити цикл по індексам елементів. Зважаючи, що наші списки - одної довжини, цей підхід дозволить нам отримати чітко те, що треба.

**Просунутий варіант.** Альтернативно можна створити цикл, який на кожній ітерації має доступ до двох елементів - по одному з кожного списка, для цього треба скористатись функцією `zip` - приклад [тут](https://realpython.com/python-zip-function/#traversing-lists-in-parallel)
</details>
"""

a = [64, 93, 60, 95, 66, 9, 15, 55, 77, 28, 74, 100, 13, 1, 85, 48, 66, 65, 59, 32]
b = [64, 93, 60, 95, 66, 9, 15, 56, 77, 28, 74, 100, 13, 1, 85, 48, 67, 65, 59, 32]

for i, x in zip(a, b):
    if i == x:
        print(True)
    else:
        print(False)

"""5. Нижче задано список `numbers`. Виконайте клітинку з його заданням.

  Давайте знайдемо середнє арифметичне значення елементів списку `numbers` округлене до 2 цифр після коми та запишемо його у змінну `numbers_mean`. Для цього виконаємо два простих кроки.

  1) Знайдіть суму всіх елементів списку `numbers` та запишіть її у змінну `numbers_sum`. Можна з використанням циклу, а можна і без.

  2) Обчисліть `numbers_mean` шляхом ділення суми елементів у списку на їх кількість. Кількість елементів в списку - це його довжина.

  Виведіть `numbers_mean`, округлений до 2 цифр після коми, на екран.

  **Підказка**: округлити число можна з використанням вбудованої функції Python [round()](https://docs.python.org/3/library/functions.html#round).
"""

numbers = [42, 51, 29, 2, 13, 44, 80, 66, 16]

numbers_sum = 0
for i in numbers:
  numbers_sum += i
numbers_mean = round(numbers_sum / len(numbers), 2)
print(numbers_mean)

"""Очікуваний результат: `38.11`

6. Задано список `a` і елемент `element`. Перевірте програмно чи є в списку `a` елемент `element` з допомогою інструкцій `if ... else`. Виведіть на екран відповідь "Так, є", якщо цей елемент в списку присутній, або "Ні, нема", якщо його там немає.
Важливо це зробити без використання імпортів будь-яких бібліотек.

  Тут цикла немає :) Але це завдання - підготовче до наступного.
"""

a = [64, 93, 60, 95, 66, 9, 15, 55, 77, 28, 74, 100, 13, 1, 85, 48, 66, 65, 59, 32]
element = 33

dcba = 0
for i in a:
  if i == element:
    dcba += 1
  else:continue
if dcba == 1:
  print("Так, є")
else:
  print("Ні, нема")

"""7. Тепер у нас не один елемент, а кілька. Вони наведені в змінній `elements`. За допомогою циклу і інструкцій `if ... else` для кожного елемента списку `elements` перевірте, чи він є в списку `a`.
Виведіть на екран відповідь "Так, є елемент <вставити значення елемента>", якщо елемент в списку присутній, або "Ні, нема елемента <вставити значення елемента>", якщо його там немає.
"""

elements = [44, 66, 77, 100]

for elem in elements:
    if elem in a:
        print(f"Так, є елемент {elem}")
    else:
        print(f"Ні, нема елемента {elem}")