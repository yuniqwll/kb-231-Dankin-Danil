# Функції для арифметичних операцій
def add(x,y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "на нуль не ділиться"
# Основна програма
def calculator():
    num1 = float(input("введіть перше число: "))
    num2 = float(input("введіть друге число: "))
    operation = input ("виберіть операцію(+, -, *, /): ")

    if operation == '+' :
        print(f"Результат: {add(num1, num2)}")
    elif operation == '-':
        print(f"Результат: {subtract(num1, num2)}")
    elif operation =='*':
        print(f"результат: {multiply(num1, num2)}")
    elif operation =='/':
        print(f"результат: {divide(num1, num2)}")
    else:
        print("невірна операція")
# колькулятор
calculator()