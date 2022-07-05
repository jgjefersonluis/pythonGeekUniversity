from datetime import datetime

from dateutil import tz

tzAC = tz.gettz('America/Eirunepe')
dataAC9 = datetime(2013, 11, 9, 23, 59, 59, tzinfo=tzAC)
dataAC10 = datetime(2013, 11, 10, 0, 0, tzinfo=tzAC)

print(dataAC9)
print(dataAC10)
