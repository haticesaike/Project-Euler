total = 0
for i in range(1,1001):
    x = i**i
    total += x
print(total % (10**10))