joltage = 0
digits = 12

with open("day-3/input.txt") as f:
    input = f.read().splitlines()

for line in input:

    num_string = line.strip()
    num_digits = len(num_string)

    delete = num_digits - digits
    stack = []

    for ch in num_string:
        d = int(ch)

        while delete > 0 and stack and stack[-1] < d:
            stack.pop()
            delete -= 1

        stack.append(d)

    best = stack[:digits]
    value = int("".join(map(str, best)))
    joltage += value

print(f"day 3 part 2: {joltage}")