joltage = 0

with open("day-3/input.txt") as f:
    input = f.read().splitlines()

for line in input:

    num_string = line.strip()
    num_digits = len(num_string)

    seen = [0] * 10
    best = 0

    for ch in num_string:
        d = int(ch)

        for p in range(9, -1, -1):
            if seen[p] > 0:
                best = max(best, 10 * p + d)
                break

        seen[d] += 1

    joltage += best

print(f"day 3 part 1: {joltage}")