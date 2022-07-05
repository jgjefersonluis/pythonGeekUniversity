'''
Mais parâmetros podem ser incluídos nas chaves de nossa sintaxe.
Use a sintaxe de código de formato {field_name: conversion},
em que field_name especifica o número de índice do argumento
para o método str.format() e a conversão se refere ao
código de conversão do tipo de dados.

Exemplo: %s – conversão de string via str() antes da formatação
'''

print("%20s" % ('geeksforgeeks',))
print("%-20s" % ('Integergeeks',))
print("%.5s" % ('Interngeeks',))

type = 'bug'
result = 'troubling'

print('I wondered why the program was %s me. Then\ it dawned on me it was a %s. '% (result, type))

match = 12000

site = 'amazon'

print("%s is so useful. I tried to look\ up mobile and they had a nice one that cost %d rupees." % (site, match))

