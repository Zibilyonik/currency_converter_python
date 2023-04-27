#Python3
import json
import requests

def load_data(url):
    response = requests.get(url)
    return json.loads(response.text)

def main():
    currency = input()
    currency_val = load_data(f'http://www.floatrates.com/daily/{currency}.json')
    print(currency_val['usd'])
    print(currency_val['eur'])


if __name__ == '__main__':
    main()