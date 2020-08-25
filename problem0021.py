def divisor(a):
    list_divisor= []
    i=1
    while (i <= a//2+1):
        if (a%i==0):
            list_divisor.append(i)
        i+=1
    return sum(list_divisor)


list_divisor=[]
for i in range(1,10000):
    x=divisor(i)
    if divisor(x) == i and x!= i:
        list_divisor.append(x)

print(sum(list_divisor))
