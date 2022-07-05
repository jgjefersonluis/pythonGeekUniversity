# https://docs.python.org/pt-br/3/library/collections.html#collections.Counter
from collections import Counter

list = [1, 1, 2, 3, 4, 5, 6, 7, 9, 2, 3, 4, 8]
ob = Counter(list)
items = ob.items()

print("The datatype is " + str(type(items)))
print(items)
for i in items:
    print(i)