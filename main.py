# Python3
'''
    receives currency code from user, then prints the exchange rate for usd, eur and try
    if left empty, defaults to pln
    
    functions:
        load_data(url) - grabs data from the provided url and returns the text
        main() - main function to grab currency values and print them

'''
import json
import requests


def load_data(url):
    '''grabs data from the provided url and returns the text'''
    response = requests.get(url, timeout="5")
    return json.loads(response.text)


def main():
    '''main function to grab currency values and print them'''
    currency = input().lower()
    if currency == "":
        currency = 'pln'
    currency_val = load_data(f'http://www.floatrates.com/daily/{currency}.json')
    print(
        f'USD: {round(currency_val["usd"]["rate"], 2)}, \
            inverse: {round(currency_val["usd"]["inverseRate"], 2)}')
    print(
        f'EUR: {round(currency_val["eur"]["rate"], 2)}, \
            inverse: {round(currency_val["eur"]["inverseRate"], 2)}')
    print(
        f'TRY: {round(currency_val["try"]["rate"], 2)}, \
            inverse: {round(currency_val["try"]["inverseRate"], 2)}')


if __name__ == '__main__':
    main()
