def reverse(n):
    reverse=0
    while (n > 0):
        x = n%10
        reverse = reverse*10 + x
        n = n//10
    return reverse

def palindrom(n):
    count = 0
    while(count < 50):
        a = reverse(n) + n
        if reverse(a) == a:
            return True
        else:
            n = a
            count += 1

    return False


count = 0
for i in range(10,10001):
    if not palindrom(i):
        count += 1

print(count)





