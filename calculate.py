# Завдання 2 (додатково)

# 1. У репозиторії `python-hw-1` стоворити файл `calculate.py` який повинен місти программу вирішення базових арифметичних операцій.
# 2. Программа повина зчитувати аргументи командної строки (за допомогою модуля `sys`) і виконувати арифметичні операції.
# 3. Необхідна підтримка 4 базових арифметичних операцій: +, -, *, /
# - додавання, віднімання, множення, ділення.
# 4. Результат виконання арифметичної операції потрібно виводити у консоль.
# 5. Программа повинна адекватно оброблювати помилки.
# 6. Программа повинна запускатись наступним чином: `python [calculate.py](http://calculate.py) 2 + 2`
# 7. Тестові запуски:
# 1. `python calculate.py 2 + 2` -> 4
# 2. `python calculate.py 2 - 200` -> -198
# 3.  `python calculate.py 2 * 8` -> 16
# 4.  `python calculate.py 200 / 2` -> 100
import sys
a = float(input("enter first number: "))
b = float(input("enter second number: "))
operation = input("watch shell i do? (+,-,/,*): ")
result = 0
if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
print(f"Total: {result}")
