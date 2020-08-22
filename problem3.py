k=0
sayı=600851475143
bölen=2
while sayı !=1:
    if(sayı%bölen==0):
        k=bölen
        sayı/=bölen
    else:
        bölen+=1
print(k)