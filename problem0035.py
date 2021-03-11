
def prime(n):
    if n== 0 or n==1:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if(n%i == 0):
            return False
    else:
        return True


def slide(p):
    k = len(str(p))
    new_number = p % 10**(k - 1)*10 + p // (10**(k - 1))
    return new_number


primes_list = [0] * 1000000
for i in range(0,1000000):
    if prime(i):
        primes_list[i] = i

count = 0
for i in primes_list:
    if i != 0:
        convert = i
        for j in range(len(str(i))):
                convert = slide(convert)
                if convert  == i:
                    count += 1
                    break
                if not primes_list[convert]:
                    break

print(count)





