class Calculator:
    def add(self, a, b):
        """Додавання"""
        return a + b

    def subtract(self, a, b):
        """Віднімання"""
        return a - b

    def multiply(self, a, b):
        """Множення"""
        return a * b

    def divide(self, a, b):
        """Ділення"""
        if b == 0:
            raise ValueError("Ділення на нуль неможливе.")
        return a / b