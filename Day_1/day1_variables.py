# Manual variable switcher

# a = 29
# b = 41

# switcher = a
# a = b
# b = switcher

# print(a, b)

# Better variant

a, b = 29, 41
a, b = b,a
print(a, b)
