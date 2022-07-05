from datetime import date

from secao19_dataHora.metodoToday import data_atual

data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)

print(data_em_texto)

data_em_texto2 = '0{}/0{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)

print(data_em_texto2)

