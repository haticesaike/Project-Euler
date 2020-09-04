ones_digit = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
other_digit = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def numbers(n):
    if n < 20:
        return ones_digit[n]
    elif n < 100:
        return other_digit[n//10] + (ones_digit[n%10] if (n%10 != 0) else"")
    elif n < 1000:
        return  ones_digit[n//100]+"hundred" + ("and" + numbers(n%100) if (n%100 != 0) else"")
    elif n == 1000:
        return "onethousand"

total = 0
for i in range (1,1001):
    total += len(numbers(i))


print(total)