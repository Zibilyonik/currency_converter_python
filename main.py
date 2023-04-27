#Python3
import json
import requests

def load_data(url):
    response = requests.get(url)
    return json.loads(response.text)

def main():
    currency = input()
    currency_val = load_data(f'http://www.floatrates.com/daily/{currency}.json')
    print(f'USD: {round(currency_val["usd"]["rate"], 2)}, inverse: {round(currency_val["usd"]["inverseRate"], 2)}')
    print(f'EUR: {round(currency_val["eur"]["rate"], 2)}, inverse: {round(currency_val["eur"]["inverseRate"], 2)}')
    print(f'TRY: {round(currency_val["try"]["rate"], 2)}, inverse: {round(currency_val["try"]["inverseRate"], 2)}')


if __name__ == '__main__':
    main()