from datetime import date, timedelta

data = date(2019, 2, 1)

dataBis = date(2020, 2, 1)

umMes = timedelta(days=+30)
print(data + umMes)


print(dataBis + umMes)
