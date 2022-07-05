def sort_idade(e):
    return e['idade']

lista_pessoas = [{'nome': 'Maria','idade': 23}, {'nome': 'João', 'idade': 19},
                 {'nome': 'Paulo', 'idade': 32}, {'nome': 'Cláudia', 'idade': 20}]
lista_pessoas.sort(key=sort_idade)

print(lista_pessoas)

lista_pessoas.sort(reverse = True, key=sort_idade)

print(lista_pessoas)
