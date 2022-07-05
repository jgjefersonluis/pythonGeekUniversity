from datetime import datetime

data = datetime.strptime('24/09/2020 22:00', '%d/%m/%Y %H:%M')
print(data)
#  2020-09-24 22:00:00

data = datetime.fromisoformat('2020-09-24T22:00')
print(data)
#  2020-09-24 22:00:00

dataSimples = datetime.strptime('13-09-2020', '%d-%m-%Y').date()
print(dataSimples)
#  2020-09-13

horaSimples = datetime.strptime('11:45:30', '%H:%M:%S').time()
print(horaSimples)
#  11:45:30