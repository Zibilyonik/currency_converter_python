
def main():
    count = input()
    values = {"RUB": 2.98, "ARS": 0.82,
              "HNL": 0.17, "AUD": 1.9622, "MAD": 0.208}
    for exchange in values.items():
        print(
            f'I will get {float(values[exchange]) * float(count)} {exchange} from the sale of {count} conicoins.')
