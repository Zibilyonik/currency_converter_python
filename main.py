# Python3
'''
    receives currency code from user, then prints the exchange rate for usd, eur and try
    if left empty, defaults to pln
    
    functions:
        load_data(url) - grabs data from the provided url and returns the text
        main() - main function to grab currency values and print them

'''
def load_data(url):
    response = requests.get(url)
    return json.loads(response.text)


def main():
    rates = {}
    currency = input()
    if currency == "":
        return
    rates[currency] = 1
    currency_val = load_data(f'http://www.floatrates.com/daily/{currency}.json')
    if currency != 'eur':
        rates['eur'] = currency_val['eur']['rate']
    if currency != 'usd':
        rates['usd'] = currency_val['usd']['rate']

    while True:
        target = input()
        if target == "":
            break
        amount = input()
        if amount == "":
            break
        print('Checking the cache...')
        if target in rates:
            print('Oh! It is in the cache!')
        else:
            print('Sorry, but it is not in the cache!')
            rates[target] = currency_val[target]['rate']
        print(f'You received {round(float(amount) * float(rates[target]), 2)} {target.upper()}.')

main()
