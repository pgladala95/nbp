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
    year = input('What year?')
    month = input('What month?')
    day = input('What day?')
    date_of_exchange = year + '-' + month + '-' + day
    flag = True  # bo nie miałem innego pomysłu
    try:
        to_retun=[nbpy.NBPClient(currency, as_float=True).date(date_of_exchange),flag]
    except Exception:
        flag = False
        to_retun = [0, flag]
        print("No data available for date")
    return to_retun