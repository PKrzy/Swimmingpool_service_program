import json


def get_path_prices():
    with open("config.json", 'r') as fh:
        path = json.load(fh)["prices_path"]
    return path


def load_prices(path):
    """Load data from file as json"""

    with open(path, 'r') as fp:
        new_data = json.load(fp)
    return new_data


class DataPrices:
    def __init__(self):
        self._prices_path = get_path_prices()
        with open(self.prices_path(), 'r') as fp:
            data = json.load(fp)
        self._data = data

    def prices_path(self):
        return self._prices_path

    def data(self):
        return self._data

    def load_new_prices(self, path):
        new_data = load_prices(path)
        with open(self.prices_path(), 'w') as file_handle:
            json.dump(new_data, file_handle, indent=4)

    def get_price(self, client, day):
        price = self.data()[day][client]
        return price

    def get_till_hour_promo(self, day):
        till_hour_promo = self.data()[day]['till_hour_promo']
        return till_hour_promo
