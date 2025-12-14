area = 0

with open("day-9/input.txt") as f:
    input = f.read().splitlines()

points = []

for line in input:    
    x, y = map(int, line.split(","))
    points.append((x, y))

n = len(points)

for i in range(n):
    x1, y1 = points[i]

    for j in range(i + 1, n):
        x2, y2 = points[j]

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if dx == 0 or dy == 0:
            continue

        candidate = (dx + 1) * (dy + 1)
        
        if candidate > area:
            area = candidate

print(f"day 9 part 1: {area}")