fn1=1
fn2=1
list=[]
total=0
while fn1 < 4000000:
    fn3=fn1+fn2
    fn1=fn2
    fn2=fn3
    list.append(fn1)
for i in list:
    if i%2==0:
        total+=i

print(total)
