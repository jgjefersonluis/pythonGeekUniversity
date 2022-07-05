from datetime import date
from dateutil.relativedelta import relativedelta

nascimento = date(1971, 9, 11)
hoje = date.today()
idade = relativedelta(hoje, nascimento)

print(idade.years)


print(idade)
