DEBUG = False

def getmin(s):
    return int(s.split('-')[0])

def getmax(s):
    return int(s.split('-')[1])


def valid_sled (min, max, token, s):
    if DEBUG: print('min: ' + str(min) + ' max: ' + str(max) + ' token: ' + str(token) + ' s: ' + str(s))
    n = 0
    for t in list(s):
        if t == token:
            n += 1
    if (min <= n and max >= n):
        return True
    else:
        return False


def valid_toboggan (pos1, pos2, token, s):
    if ((s[pos1-1] == token) ^ (s[pos2-1] == token)):
        return True
    else:
        return False


fptr = open('input', 'r')

n_sled = 0
n_toboggan = 0

for l in fptr.readlines():
    l = l.strip()
    t = l.split(' ')
    if DEBUG: print(str(t))

    if valid_sled(getmin(t[0]), getmax(t[0]), t[1][0], t[2]):
        n_sled += 1

    if valid_toboggan(getmin(t[0]), getmax(t[0]), t[1][0], t[2]):
        n_toboggan += 1


print(str(n_sled))
print(str(n_toboggan))



