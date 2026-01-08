a = 42  # Initial assignment
b = a  # b points to the same object in memory as a
c = a  # c points to the same object in memory as a
a = 10  # a is reassigned to point to a new object in memory
b = c  # b points to the same object in memory as c

print(a, b, c)
# Expected output:
# 10 42 42
