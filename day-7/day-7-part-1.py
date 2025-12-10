splits = 0

with open("day-7/input.txt") as f:
    input = f.read().splitlines()

rows = len(input)
cols = len(input[0])

s = input[0].index('S') if 'S' in input[0] else None
active = [s]

for r in range (1, rows):
    new_beams = set()

    for c in active:
        if 0 <= c < cols:
            if input[r][c] == '^':
                splits += 1

                if c - 1 >= 0:
                    new_beams.add(c - 1)
                if c + 1 < cols:
                    new_beams.add(c + 1)
            else:
                new_beams.add(c)

    active = new_beams

print(f"day 7 part 1: {splits}")