import requests

actual_currency = str(input())

rates_cache = {}


def get_rate(currency, new_currency):  # gets rates info from website
    rate = requests.get(f'http://www.floatrates.com/daily/{currency.lower()}.json').json()[new_currency]['rate']
    rates_cache[new_currency] = rate
    return rate


if actual_currency != 'usd':
    get_rate(actual_currency, 'usd')
if actual_currency != 'eur':
    get_rate(actual_currency, 'eur')

while True:
    exchange_currency = str(input()).lower()
    if exchange_currency == "":
        break
    else:
        amount_money = float(input())
        print("Checking the cache...")
        if exchange_currency in rates_cache:
            print("Oh! It is in the cache!")
        elif exchange_currency not in rates_cache:
            print("Sorry, but it is not in the cache")
            get_rate(actual_currency, exchange_currency)
        result = amount_money * rates_cache[exchange_currency]
        print(f"You received {round(result, 2)} {exchange_currency.upper()}")
