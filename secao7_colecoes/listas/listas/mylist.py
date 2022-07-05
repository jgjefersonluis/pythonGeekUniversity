my_list = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Carl'},
]

for entry in my_list:
    print(entry['id'])
    print(entry['name'])

my_ids = [
    {'dataset': 'e83152bc-2606-4e90-97e7-43bbf82c01fd'}
]

for entry in my_ids:
    print(entry['dataset'],['e83152bc-2606-4e90-97e7-43bbf82c01fd'])

mya_list = ['a', 'b', 'c']

print(mya_list)
print(type(my_list))
print(isinstance(my_list, list))