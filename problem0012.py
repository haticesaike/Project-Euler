def divisor_num(a):
    list_divisor= []

    for i in range(1,int(a**0.5)+1):

        if (a%i==0):
            list_divisor.append(i)
    if i**2==a:
        return len(list_divisor)*2-1

    return len(list_divisor)*2

x=1
counter=2
while(divisor_num(x) <500):
    x = x + counter
    counter = counter + 1
print(x)

