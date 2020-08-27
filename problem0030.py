def fifth_powers(n):

    total = 0
    while n != 0:
            total += (n%10)**5
            n = n//10
    return total

def is_it_equal(n):

    if fifth_powers(n) == n :
        return True
    else:
        return False

total = 0

for i in range(2,((9**5)*6)):
    if is_it_equal(i):
        total += i

print(total)



