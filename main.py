from functions import import_code, import_date
from datetime import datetime, timedelta
from decimal import Decimal

#print(nbpy.currencies)
currency = import_code()
how_much = float(input(f"How many {currency} do you want exchange?"))
different_date = int(input('Do you what current exchange course?(1) Or historical?(2)'))
rate = 0
if(different_date == 1):
    rate = nbpy.NBPClient(currency, as_float=True).current()    #as_float zmienia klasę 'decimal.Decimal' na 'float' i program się nie wysypuje
elif(different_date == 2):
    is_date_correct = False
    while is_date_correct is not True:
        rate_and_flag=import_date(currency)
        rate=rate_and_flag[0]
        is_date_correct=rate_and_flag[1]
else:
    print('Wrong option')
pln = (rate * how_much)['mid']
print(f'''
You exchange {currency} to PLN
{how_much}{currency} is {pln}PLN
''')