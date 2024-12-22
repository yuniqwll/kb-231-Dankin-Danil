import requests

def get_exchange_rate(currency):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['rate']
    else:
        print("Помилка отримання даних від API НБУ.")
        return None

def convert_currency():
    supported_currencies = {"USD", "EUR", "PLN"}
    currency = input("Введіть валюту (USD, EUR, PLN): ").upper()
    
    if currency not in supported_currencies:
        print("Некоректна валюта.")
        return

    try:
        amount = float(input("Введіть кількість валюти: "))
    except ValueError:
        print("Некоректна кількість.")
        return

    rate = get_exchange_rate(currency)
    if rate:
        result = amount * rate
        print(f"{amount} {currency} = {result:.2f} грн за курсом {rate:.2f} грн/{currency}.")

convert_currency()