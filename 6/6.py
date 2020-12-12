DEBUG = False

def intersection(a, b):
    return [c for c in a if c in b]

counts_any = []
counts_all = []
y_any = []
y_all = []
first = True

fptr = open('input', 'r')

for l in fptr.readlines():
    l = l.strip()

    if (l == ''):
        if DEBUG:
            print(str('y_any = ' + str(y_any) + ' y_all = ' + str(y_all)))
        counts_any.append(len(y_any))
        counts_all.append(len(y_all))
        y_any = []
        y_all = []
        first = True
        continue

    for c in l:
        if c not in y_any:
            y_any.append(c)

    if first == True:
        y_all = [c for c in l] 
        first = False
    else:
        y_all = intersection([c for c in l], y_all)
    if DEBUG: print(str(y_all))


if DEBUG: 
    print('any = ' + str(counts_any))
    print('all = ' + str(counts_all))

print(str(sum(counts_any)))
print(str(sum(counts_all)))

