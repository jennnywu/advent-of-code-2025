with open("day-8/input.txt") as f:
    input = f.read().splitlines()

points = []
for line in input:
    x, y, z = map(int, line.split(","))
    points.append((x, y, z))

def distance(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dz = a[2] - b[2]
    
    return ((dx ** 2) + (dy ** 2) + (dz ** 2)) ** 0.5

pairs = []
n = len(points)

for i in range(n):
    for j in range(i + 1, n):
        d = distance(points[i], points[j])
        pairs.append((d, i, j))

pairs.sort()

parent = list(range(n))
size = [1] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra != rb:
        if size[ra] < size[rb]:
            ra, rb = rb, ra

        parent[rb] = ra
        size[ra] += size[rb]

        return True
    
    return False

circuits = n
last_a = None
last_a = None

for d, i, j in pairs:
    if union(i, j):
        circuits -= 1

        if circuits == 1:
            last_a = i
            last_b = j
            break

x1 = points[last_a][0]
x2 = points[last_b][0]

answer = x1 * x2

print(f"day 8 part 1: {answer}")