from math import factorial
x = factorial(100)

total = 0
while x != 0:
    total += x % 10
    x = x // 10

print(total)
