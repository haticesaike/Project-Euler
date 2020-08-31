def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i == 0):
            return False
    else:
        return True

total = 2
for i in range(3,2000000,2):
    if prime(i):
        total = total + i

print(total)