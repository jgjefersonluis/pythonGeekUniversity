contatos_lista = [
    ('Yan', '1234-5678'),
    ('Pedro', '9999-9999'),
    ('Ana', '8765-4321'),
    ('Marina', '8877-7788')
]

contatos = dict(contatos_lista)
print(contatos)
print('Yan' in contatos)
print('9999-9999' in contatos)
print('9999-9999' in contatos.values())
contatos['João'] = '8887-7778'
print(contatos)
contatos['GOW'] = '6667-7778'
print(contatos)
del contatos['GOW']
print(contatos)
