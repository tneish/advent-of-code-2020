DEBUG = False
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)


def aug(l, d):
    if l == '': return False
    l = l.split(' ')
    for i in l:
        t = i.split(':')
        d[t[0]] = t[1]
    return True

def least_most(l, m, n):
    return n >= l and n <= m

def valid_byr(d):
    #four digits; at least 1920 and at most 2002.
    return least_most(1920, 2002, int(d['byr']))

def valid_iyr(d):
    #four digits; at least 2010 and at most 2020.
    return least_most(2010, 2020, int(d['iyr']))

def valid_eyr(d):
    #four digits; at least 2020 and at most 2030.
    return least_most(2020, 2030, int(d['eyr']))

def valid_hgt(d):
    #- a number followed by either cm or in:
    #    If cm, the number must be at least 150 and at most 193.
    #    If in, the number must be at least 59 and at most 76.
    t = d['hgt']
    if (t[-1] == 'm'):
        return least_most(150, 193, int(t[0:-2]))
    elif (t[-1] == 'n'):
        return least_most(59, 76, int(t[0:-2]))
    else:
        return False

def valid_hcl(d):
    #a # followed by exactly six characters 0-9 or a-f.
    t = d['hcl']
    valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    if (t[0] != '#'): return False
    for c in t[1:]:
        if (c not in valid): return False
    return True

def valid_ecl(d):
    #exactly one of: amb blu brn gry grn hzl oth
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if d['ecl'] in valid:
        return True
    else:
        return False


def valid_pid(d):
    #a nine-digit number, including leading zeroes.
    t = d['pid']    
    valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if (len(t) != 9): return False
    for c in t:
        if c not in valid: return False
    return True


def fields_present(r):
    k = r.keys()
    if (('byr' in k) and
        ('iyr' in k) and
        ('eyr' in k) and
        ('hgt' in k) and
        ('hcl' in k) and
        ('ecl' in k) and
        ('pid' in k)):
        return 1
    else:
        return 0

def fields_valid(r):
    k = r.keys()
    if (('byr' in k) and valid_byr(r) and
        ('iyr' in k) and valid_iyr(r) and
        ('eyr' in k) and valid_eyr(r) and
        ('hgt' in k) and valid_hgt(r) and
        ('hcl' in k) and valid_hcl(r) and
        ('ecl' in k) and valid_ecl(r) and
        ('pid' in k) and valid_pid(r)):
        return 1
    else:
        return 0


r = {}
n_valid1 = 0
n_valid2 = 0

fptr = open('input', 'r')
for l in fptr.readlines():
    l = l.strip()
    if aug(l, r):
        continue
    else:
        if DEBUG: print('new record: ' + str(r))
        n_valid1 += fields_present(r)
        n_valid2 += fields_valid(r)
        r = {}


print(str(n_valid1))
print(str(n_valid2))

