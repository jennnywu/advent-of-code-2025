with open("day-7/input.txt") as f:
    input = f.read().splitlines()

rows = len(input)
cols = len(input[0])

s = input[0].index('S') if 'S' in input[0] else None

active = [0] * cols
active[s] = 1

for r in range(1, rows):
    new_active = [0] * cols

    for c in range(cols):
        splits = active[c]

        if splits == 0:
            continue

        if input[r][c] == '^':
            if c - 1 >= 0:
                new_active[c - 1] += splits
            if c + 1 < cols:
                new_active[c + 1] += splits
        else:
            new_active[c] += splits

    active = new_active

splits = sum(active)

print(f"day 7 part 2: {splits}")