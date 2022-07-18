from multiprocessing.sharedctypes import Value
import sys
from turtle import left

# print(sys.argv)

if len(sys.argv) != 4:
    print("Arg len is 4")
    sys.exit()

# print(sys.argv№)
# +,-,/,*
#['python-hw-1/calculate1.py', '2', '+', '2']
# [шлях до файлу] [лівий операнд] [ариф опер] [правий операнд]

# PEP-8

left_operand = sys.argv[1]
right_operand = sys.argv[3]

operation = sys.argv[2]

allowed_operations = ["+", "-", "*", "/"]  # перевірка на доступні операції

# if operation != "+" and operation != "-":
if operation not in allowed_operations:
    print("operation is not allowed")
    sys.exit()  # після єтого все что дальше робиться не буде

try:
    left_operand = int(left_operand)
    right_operand = int(right_operand)
except ValueError:
    print("Left and right operand must be int")
    sys.exit()

if operation == "/" and right_operand == 0:
    print("Division by zero is not allowed")

"""if operation == "*":
    print(left_operand * right_operand)
elif operation == "+":
    print(left_operand + right_operand)"""


"""match operation:
    case "*":
        print(left_operand * right_operand)   второй вариант"""

'''
print(eval(f"{left_operand}{operation}{right_operand}"))
'''

# if "2".isdigit():

"""print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])"""
