num=set()
for a in range(2,101):
    for b in range(2,101):
        num.add(a**b)
print(len(num))
