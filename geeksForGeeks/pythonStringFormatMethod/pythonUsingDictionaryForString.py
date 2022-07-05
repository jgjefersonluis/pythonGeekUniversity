'''
Usando um dicionário para formatação de string
Usando um dicionário para descompactar valores nos espaços reservados
na string que precisa ser formatada. Basicamente usamos ** para
descompactar os valores. Este método pode ser útil na substituição
de strings ao preparar uma consulta SQL.
'''

introduction = "My name is {first_name} {middle_name} {last_name}"
full_name = {
    'first_name': 'Tony',
    'middle_name': 'Howard',
    'last_name': 'Stark',
    'aka': 'Iron Man',
}

# Notice the use of "**" operator to unpack the values.
print(introduction.format(**full_name))


