from datetime import date

from dateutil.relativedelta import relativedelta

data = date(2019, 2, 1)
dataBis = date(2020, 2, 1)

umMes = relativedelta(months=+1)
print(data + umMes)


print(dataBis + umMes)
