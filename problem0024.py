from itertools import permutations

permutations = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

digits = []
for i in permutations[999999]:
    digits.append(str(i))

value = ''.join(digits)

print(value)