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
from ast import operator
import math
import sys

left_operand = sys.argv[1]
right_operand = sys.argv[3]
operation = sys.argv[2]
allowed_operations = ["+", "-", "*", "/", "%"]

print("Number of arguments:", len(sys.argv), "arguments")
print("Argument List:", str(sys.argv))

if len(sys.argv) != 4:
    print("Arg len should be 4")
    sys.exit()

if operation == "/" and right_operand == 0:
    print("Division by zero is not allowed")
    sys.exit()

if operation not in allowed_operations:
    print("operation is not allowed")
    sys.exit()

try:
    left_operand is not int(left_operand)
    right_operand is not int(right_operand)
except ValueError:
    print("Left and right operand must be int")
    sys.exit()

match operation:
    case "+":
        print(int(left_operand) + int(right_operand))
    case "-":
        print(int(left_operand) - int(right_operand))
    case "*":
        print(int(left_operand) * int(right_operand))
    case "/":
        print(int(left_operand) / int(right_operand))
    case "%":
        print(int(left_operand) % int(right_operand))
        

#print((f"{left_operand} {operation} {right_operand}"), "=", eval(f"{left_operand}{operation}{right_operand}"))


