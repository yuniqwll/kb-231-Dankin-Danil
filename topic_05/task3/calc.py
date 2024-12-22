from functions import add, subtract, multiply, divide
from operations import get_number, get_operation

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

while True:
    calculator()
    choice = input("Натисніть 'E' для виходу або будь-яку іншу клавішу для продовження: ").lower()
    if choice == 'e':
        print("Завершення програми.")
        break