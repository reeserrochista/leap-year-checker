from datetime import date
year = int(input('What year you want to analyze?. Type 0 to see today year'))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))

