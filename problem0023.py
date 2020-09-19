def total_divisor(x):
    numbers = set()
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            numbers.add(i)
            if i != 1:
                numbers.add(int(x/i))
    return sum(numbers)


def abundant(n):
    if total_divisor(n) > n:
        return True
    else:
        return False

abundant_numbers = []
for i in range(1,28124):
    if abundant(i):
        abundant_numbers.append(i)

total_abundant_numbers = [0]*28124
for i in range(0,len(abundant_numbers)):
    for j in range(0,i+1):
        x = abundant_numbers[i] + abundant_numbers[j]
        if x <= 28123:
            total_abundant_numbers[x] = 1
        else:
            break

total = 0
for i in range(0,len(total_abundant_numbers)):
    if total_abundant_numbers[i] == 0:
        total += i

print(total)