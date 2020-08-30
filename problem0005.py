def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i == 0):
            return False
    else:
        return True

total = 1
for i in range(1,21):
    if prime(i):
        total = total*i
for i in range(1,21):
    if(i**2 < 20):
        total = total*i

print(total)