#код калькулятора з обробкою винятків

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Помилка: на нуль ну ділиться"

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введіть число!")

def get_operation():
    valid_operations = {'+', '-', '*', '/'}
    while True:
        operation = input("Виберіть операцію (+, -, *, /): ")
        if operation in valid_operations:
            return operation
        print("Помилка: виберіть правильну операцію!")

def calculator():
    num1 = get_number("Введіть перше число: ")
    num2 = get_number("Введіть друге число: ")
    operation = get_operation()

    match operation:
        case '+':
            print(f"Результат: {add(num1, num2)}")
        case '-':
            print(f"Результат: {subtract(num1, num2)}")
        case '*':
            print(f"Результат: {multiply(num1, num2)}")
        case '/':
            print(f"Результат: {divide(num1, num2)}")

# цикл
while True:
    calculator()
    choice = input("Натисніть 'E' для виходу або будь-яку іншу клавішу для продовження: ").lower()
    if choice == 'e':
        print("Завершення програми.")
        break
