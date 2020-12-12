DEBUG = True

def bin_to_dec(s):
    s = s.replace('F', '0')
    s = s.replace('B', '1')
    s = s.replace('L', '0')
    s = s.replace('R', '1')
    return int(s, 2)


max_seatid = -1
my_seatid = -1
seatids = []

fptr = open('input', 'r')

for l in fptr.readlines():
    l = l.strip()

    r = bin_to_dec(l[:7])
    c = bin_to_dec(l[7:])

    seatid = (r * 8) + c
    if DEBUG: print('r: ' + str(r) + ' c: ' + str(c) + ' id: ' + str(seatid))

    seatids.append(seatid)

    if (seatid > max_seatid):
        max_seatid = seatid

seatids.sort()
if DEBUG:
    print('Seat IDs:')
    for i in seatids:
        print(str(i))

for i in range(1, len(seatids)):
    if seatids[i] != seatids[i-1] + 1:
        my_seatid = seatids[i-1] + 1
        break 

print(str(max_seatid))
print(str(my_seatid))

