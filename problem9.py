for i in range(1,1000):
    for j in range(i+1,1000):
        k=(i**2+j**2)**0.5
        if i+j+k==1000:
            print(int(i*j*k))