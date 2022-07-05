from datetime import datetime, timedelta

data = datetime(2019, 2, 28)
dataBis = datetime(2020, 2, 28)

tDelta = timedelta(hours=+30)
print(data + tDelta)


print(dataBis + tDelta)


tDelta = timedelta(hours=-3)
print(dataBis + tDelta)
