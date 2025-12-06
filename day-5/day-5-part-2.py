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

ranges.sort()

merged = []

for lo, hi in ranges:
    if not merged:
        merged.append([lo, hi])
    else:
        prev_lo, prev_hi = merged[-1]
        if lo <= prev_hi + 1:
            merged[-1][1] = max(prev_hi, hi)
        else:
            merged.append([lo, hi])

for lo, hi in merged:
    count += hi - lo + 1

print(f"day 5 part 2: {count}")