import nbpy     #mogą być przestarzałe biblioteki (problem z utylis.py -> colections zmienić na collections.abc)
from datetime import datetime, timedelta
from decimal import Decimal

#print(nbpy.currencies)
currency = 'abc'
while (not currency in nbpy.currencies):
    currency = input('What currency do you want exchange?(ISO code)').upper()
    if not currency in nbpy.currencies:
        print('This is not ISO currency code')
how_much = float(input(f"How many {currency} do you want exchange?"))
different_date = int(input('Do you what current exchange course?(1) Or historical?(2)'))
rate = 0
if(different_date == 1):
    rate = nbpy.NBPClient(currency, as_float=True).current()    #as_float zmienia klasę 'decimal.Decimal' na 'float' i program się nie wysypuje
elif(different_date == 2):
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
    rate = nbpy.NBPClient(currency, as_float=True).date(date_of_exchange)
else:
    print('Wrong option')
pln = (rate * how_much)['mid']
print(f'''
You exchange {currency} to PLN
{how_much}{currency} is {pln}PLN
''')