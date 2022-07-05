from datetime import date, datetime
from dateutil.relativedelta import relativedelta

hoje = date.today()
umDia = relativedelta(days=+1)
amanha = hoje + umDia

print(hoje)


print(amanha)


agora = datetime.now()
menosUmaHora = relativedelta(hours=-1)
umaHoraAtras = agora + menosUmaHora

print(agora)


print(umaHoraAtras)
