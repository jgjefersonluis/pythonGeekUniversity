lista_nomes = ['Maria', 'João', 'Paulo', 'Cláudia']

try:
    lista_nomes.remove("José")
except ValueError:
    print("Item não existe")