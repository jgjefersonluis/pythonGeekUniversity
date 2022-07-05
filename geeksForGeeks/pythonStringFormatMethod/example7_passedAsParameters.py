# To demonstrate spacing when
# strings are passed as parameters
print("{0:4}, is the computer science portal for {1:8}!"
      .format("GeeksforGeeks", "geeks"))

# To demonstrate spacing when numeric
# constants are passed as parameters.
print("It is {0:5} degrees outside!"
      .format(40))

# To demonstrate both string and numeric
# constants passed as parameters
print("{0:4} was founded in {1:16}"
      .format("GeeksforGeeks", 2022))
# To demonstrate aligning of spaces
print("{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2022))

print("{:*^20s}".format("Geeks"))
