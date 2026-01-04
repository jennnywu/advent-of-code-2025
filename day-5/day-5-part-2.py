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

start, end = ranges[0]

for i in ranges[1:]:
    next_start, next_end = i

    if next_start <= end:
        end = max(end, next_end)
    else:
        count += end - start + 1
        start, end = next_start, next_end

count += end - start + 1

print(f"day 5 part 2: {count}")