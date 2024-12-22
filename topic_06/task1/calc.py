import logging
from functions import add, subtract, multiply, divide
from operations import get_number, get_operation

# Налаштування логування
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

def calculator():
    num1 = get_number("Введіть перше число: ")
    num2 = get_number("Введіть друге число: ")
    operation = get_operation()

    match operation:
        case '+':
            result = add(num1, num2)
        case '-':
            result = subtract(num1, num2)
        case '*':
            result = multiply(num1, num2)
        case '/':
            result = divide(num1, num2)
    
    print(f"Результат: {result}")
    # Запис до лог-файлу
    logging.info(f"Операція: {operation}, Числа: {num1}, {num2}, Результат: {result}")

while True:
    calculator()
    choice = input("Натисніть 'E' для виходу або будь-яку іншу клавішу для продовження: ").lower()
    if choice == 'e':
        print("Завершення програми.")
        break