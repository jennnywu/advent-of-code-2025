num = 50
count = 0

with open("day-1/input.txt") as f:
    input = f.read().splitlines()

for line in input:
    direction = line[0]
    steps = int(line[1:])

    sign = 1 if direction == 'R' else -1

    num = (num + (sign * steps)) % 100
    if num == 0:
        count += 1

print(f"day 1 part 1: {count}")
