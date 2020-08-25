even = lambda x:x/2
odd = lambda  x:x*3+1
def chain(x):
    counter = 0
    while x != 1:
        if (x%2 == 0):
            x = even(x)
        else:
            x = odd(x)
        counter += 1
    return counter

x=0
max_chain=0
for i in range(1,1000001):
    if chain(i) > max_chain:
        max_chain=chain(i)
        x=i
print(x)


