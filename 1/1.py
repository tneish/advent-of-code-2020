import itertools

fptr = open('input', 'r')

lstripped = []
for line in fptr.readlines():
    lstripped.append(line.strip())

for c in itertools.combinations(lstripped, 2):
    first = int(c[0])
    second = int(c[1])
    if (first + second == 2020):
        print(str(first * second))

for c in itertools.combinations(lstripped, 3):
    first = int(c[0])
    second = int(c[1])
    third = int(c[2])
    if (first + second + third == 2020):
        print(str(first * second * third))
