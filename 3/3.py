def count_hits(n_right, n_down):
    hits = 0
    x = n_right
    y = n_down

    while y < len(lines):
        lookup_x = x % len(lines[y])
        if (lines[y][lookup_x] == '#'):
            hits += 1
        x += n_right
        y += n_down

    return hits


lines = []

fptr = open('input', 'r')
for line in fptr.readlines():
    lines.append(line.strip())

print(str(count_hits(3, 1)))

print(str(count_hits(1, 1) * \
    count_hits(3, 1) * \
    count_hits(5, 1) * \
    count_hits(7, 1) * \
    count_hits(1, 2)))

