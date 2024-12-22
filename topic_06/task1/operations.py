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