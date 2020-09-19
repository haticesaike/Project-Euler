def digit(n):
    digit_value = 0
    while n != 0:
        n = n//10
        digit_value +=1
    return digit_value


fn1 = 1
fn2 = 1
count = 2
while True:
    fn3 = fn1 + fn2
    fn1 = fn2
    fn2 = fn3
    count += 1
    if digit(fn2) == 1000:
        print(count)
        break