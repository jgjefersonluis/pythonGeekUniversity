from collections import Counter

list = [1, 1, 2, 3, 4, 5,
        6, 7, 9, 2, 3, 4, 8]
ob = Counter(list)
keys = ob.keys()

print("The datatype is "
      + str(type(keys)))
print(keys)
for i in keys:
    print(i)