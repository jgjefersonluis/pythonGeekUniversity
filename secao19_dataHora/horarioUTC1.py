from dateutil import tz
from datetime import datetime

data = datetime(2020, 9, 24, 22, 10, 30, tzinfo=tz.tzlocal())
print(data)


print(data.tzname())
