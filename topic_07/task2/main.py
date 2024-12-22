from core import Calculator
from utils import get_number

def main():
    calc = Calculator()
    while True:
        print("\n--- Калькулятор ---")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Вихід")
        
        choice = input("Оберіть операцію (1-5): ")
        
        if choice == '5':
            print("Дякуємо за використання калькулятора!")
            break

        if choice in {'1', '2', '3', '4'}:
            num1 = get_number("Введіть перше число: ")
            num2 = get_number("Введіть друге число: ")
            
            try:
                if choice == '1':
                    result = calc.add(num1, num2)
                    operation = "+"
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    operation = "-"
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                    operation = "*"
                elif choice == '4':
                    result = calc.divide(num1, num2)
                    operation = "/"
                
                print(f"Результат: {num1} {operation} {num2} = {result}")
            except ValueError as e:
                print(f"Помилка: {e}")
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()