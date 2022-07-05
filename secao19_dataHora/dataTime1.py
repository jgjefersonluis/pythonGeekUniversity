from datetime import date, time, datetime

dataSimples = date(year=2020, month=9, day=24)
print(dataSimples)
#  2020-09-24

hora = time(hour=22, minute=10, second=30)
print(hora)
#  22:10:30

data = datetime(year=2020, month=9, day=24, hour=22, minute=10, second=30)
print(data)
#  2020-09-24 22:10:30
dataCompleta = datetime.combine(dataSimples, hora)
print(dataCompleta)
#  2020-09-24 22:10:30