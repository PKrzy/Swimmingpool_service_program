from prices.prices_data import DataPrices, load_prices
import json


def test_load_prices():
    data = load_prices('tests/test_prices.json')
    assert data == {
        "Monday": {
            "Adult": 15,
            "Kid": 10,
            "Kid_under_5_years_old": 8,
            "Disabled": 5,
            "Pensioner": 10,
            "Student": 10,
            "till_hour_promo": 15,
            "swimming_school": 30
        }}


def test_prices_path():
    path = DataPrices().prices_path()
    assert path == 'prices/prices.json'


def test_prices_data(monkeypatch):
    def fake_path(d):
        return 'tests/test_prices.json'
    monkeypatch.setattr(DataPrices, 'prices_path', fake_path)
    data = DataPrices().data()
    assert data == {
        "Monday": {
            "Adult": 15,
            "Kid": 10,
            "Kid_under_5_years_old": 8,
            "Disabled": 5,
            "Pensioner": 10,
            "Student": 10,
            "till_hour_promo": 15,
            "swimming_school": 30
        }}


def test_get_prices(monkeypatch):
    def fake_path(d):
        return 'tests/test_prices.json'
    monkeypatch.setattr(DataPrices, 'prices_path', fake_path)
    price = DataPrices().get_price("Kid", 'Monday')
    price_2 = DataPrices().get_price("Disabled", 'Monday')
    assert price == 10
    assert price_2 == 5


def test_get_till_hour_promo(monkeypatch):
    def fake_path(d):
        return 'tests/test_prices.json'
    monkeypatch.setattr(DataPrices, 'prices_path', fake_path)
    promo = DataPrices().get_till_hour_promo('Monday')
    assert promo == 15


def test_new_prices(monkeypatch):
    def fake_path(d):
        return 'tests/test_new_prices.json'
    monkeypatch.setattr(DataPrices, 'prices_path', fake_path)
    DataPrices().load_new_prices('tests/test_prices.json')
    fp = open('tests/test_new_prices.json', 'r')
    data = json.load(fp)
    fh = open('tests/test_prices.json', 'r')
    expected_data = json.load(fh)
    assert data == expected_data
