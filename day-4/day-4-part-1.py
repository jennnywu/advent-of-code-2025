count = 0

with open("day-4/input.txt") as f:
    input = f.read().splitlines()

rows = len(input)
cols = len(input[0])

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1), (1, 0), (1, 1)
]

for r in range(rows):
    for c in range(cols):
        if input[r][c] == '@':
            neighbours = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if input[nr][nc] == '@':
                        neighbours += 1

            if neighbours < 4:
                count += 1

print(f"day 4 part 1: {count}")