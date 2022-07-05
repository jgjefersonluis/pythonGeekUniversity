"""
se parece com um dicionário, exceto pelo fato de que se você acessar uma chave que não existe,
um novo valor pode ser gerado automaticamente.
Quando você cria um defaultdict, fornece uma função usada para criar valores.
Uma função usada para criar objetos às vezes é chamada de factory (fábrica).
As funções integradas que criam listas, conjuntos e outros tipos podem ser usadas como fábricas:
"""

from collections import defaultdict
from inspect import signature

d = defaultdict(list)
print(d)

def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d