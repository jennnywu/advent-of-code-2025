with open("day-7/input.txt") as f:
    grid = f.read().splitlines()

rows = len(grid)
cols = len(grid[0])

# starting column
start = grid[0].index("S")

# list, not set, because beams do not merge in Part 2
active = [start]

# simulate down the grid
for r in range(1, rows):
    new_active = []
    for c in active:
        if 0 <= c < cols:
            if grid[r][c] == '^':
                # split into left and right
                if c - 1 >= 0:
                    new_active.append(c - 1)
                if c + 1 < cols:
                    new_active.append(c + 1)
            else:
                # continue downward
                new_active.append(c)
    active = new_active

print(len(active))
