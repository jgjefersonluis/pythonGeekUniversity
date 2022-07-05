pessoas = [({'nome': 'João', 'cidade': 'Belo Horizonte'}),
                     ({'nome': 'Maria', 'cidade': 'São Paulo'}),
                     ({'nome': 'Pedro', 'cidade': 'Curitiba'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    if pessoa['nome'] == 'Maria':
        continue
    print(contador)
    print(pessoa['nome'], "mora em", pessoa['cidade'])