import nbpy     #mogą być przestarzałe biblioteki (problem z utylis.py -> colections zmienić na collections.abc)
from datetime import datetime, timedelta
from decimal import Decimal

def import_code():
    currency = 'abc'
    while (not currency in nbpy.currencies):
        currency = input('What currency do you want exchange?(ISO code)').upper()
        if not currency in nbpy.currencies:
            print('This is not ISO currency code')
    return currency

def import_date(currency):
    is_date_correct = False
    while not is_date_correct:
        year = input('What year?')
        month = input('What month?')
        day = input('What day?')
        date_of_exchange = year + '-' + month + '-' + day
        is_date_correct = True  # bo nie miałem innego pomysłu
        try:
            nbpy.NBPClient(currency).date(date_of_exchange)
        except:
            print("No data available for date")
            is_date_correct = False
    return nbpy.NBPClient(currency, as_float=True).date(date_of_exchange)