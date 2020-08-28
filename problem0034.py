def factorial(n):

    value = 1
    for i in range(n):
        value = value*(i+1)
    return value

def total_factorial(n):

    total = 0
    while n != 0 :
        total += factorial(n%10)
        n = n//10
    return total

total = 0
x = (factorial(9))*7
for i in range(3,x+1):
    if  total_factorial(i) == i:
        total += i
print(total)