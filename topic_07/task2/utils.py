def get_number(prompt):
    """Отримує число від користувача, обробляючи помилки вводу."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введіть число.")