from datetime import datetime

data = datetime(year=2020, month=9, day=24, hour=22, minute=10, second=30)
print(data.strftime('%d/%m/%Y %H:%M:%S'))


print(data.strftime('%d-%m-%Y %H:%M'))


print(data.isoformat())
