def prime(x):
    if (x==1):
        return False
    if (x==2):
        return True
    a=2
    while True:
        if(x%a==0):
            return False
        a+=1
        if(x**0.5<a):
            return True

x=1
list=list()
while len(list) < 10001:
    if(prime(x)):
        list.append(x)
    x+=1

print(max(list))
