import json
import requests
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    #метод конвертер валюты (base  - базовая валюта, quote - валюта,  в которую пересчитываем, amount - количество валюты для пересчёта)
    #метод возвращает пересчитанную сумму
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Для конвертации задана одна и та же валюта "{base}"')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise ConvertionException(f'Валюта "{base}" не найдена!')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise ConvertionException(f'Валюта "{quote}" не найдена!')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество "{amount}"')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[keys[quote]] * amount


        return total_base
