# https://docs.python.org/3/library/collections.html
from collections import Counter

list = [1, 1, 2, 3, 4, 5,
        6, 7, 9, 2, 3, 4, 8]
ob = Counter(list)
values = ob.values()

print("The datatype is "
      + str(type(values)))
print(values)
for i in values:
    print(i)