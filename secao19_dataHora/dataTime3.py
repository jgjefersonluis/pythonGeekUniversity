from datetime import datetime, date

data = date.today()
print(data)
#  2020-09-25

data = datetime.now()
print(data)
#  2020-09-25 21:18:06.694389

timestamp = 1600995600
data = datetime.fromtimestamp(timestamp)
print(data)
#  2020-09-24 22:00:00