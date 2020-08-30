def reverse(n):
    reverse=0
    while (n > 0):
        x = n%10
        reverse = reverse*10 + x
        n = n//10
    return reverse


def palindrome(n):
        if reverse(n) == n:
            return True
        else:
            return False

list=[]
for i in range(100,1000):
    for j in range(100,1000):
        if palindrome(i*j):
            list.append(i*j)
print(max(list))
