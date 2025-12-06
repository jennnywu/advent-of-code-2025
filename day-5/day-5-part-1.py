count = 0

with open("day-5/input.txt") as f:
    input = f.read().splitlines()

i = 0
ranges = []

while i < len(input) and input[i].strip() != "":
    line = input[i].strip()
    if "-" in line:
        a, b = input[i].split("-")
        ranges.append((int(a), int(b)))
    i += 1

i += 1

ids = [int(x) for x in input[i:]]

for ingredients_id in ids:
    fresh = False
    for lo, hi in ranges:
        if lo <= ingredients_id <= hi:
            fresh = True
            break

    if fresh:
        count += 1

print(f"day 5 part 1: {count}")