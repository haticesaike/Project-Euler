total=0
totalsquare=0

for i in range(1,101):
    totalsquare+=i**2
    total+=i
print(total**2 - totalsquare)