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
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    operation = input("Виберіть операцію (+, -, *, /): ")

    match operation:
        case '+':
            print(f"Результат: {add(num1, num2)}")
        case '-':
            print(f"Результат: {subtract(num1, num2)}")
        case '*':
            print(f"Результат: {multiply(num1, num2)}")
        case '/':
            print(f"Результат: {divide(num1, num2)}")
        case _:
            print("Невірна операція")
# колькулятор
calculator()