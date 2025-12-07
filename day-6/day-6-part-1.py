solution = 0

with open("day-6/input.txt") as f:
    input = f.read().splitlines()

rows = len(input)
cols = len(input[0])

def is_blank_column(c):
    for r in range(rows):
        if input[r][c] != " ":
            return False
    return True

c = 0

while c < cols:
    if is_blank_column(c):
        c += 1
        continue

    start = c

    while c < cols and not is_blank_column(c):
        c += 1
    end = c

    op_row = input[rows - 1][start:end]
    op = "+" if "+" in op_row else "*"

    numbers = []

    for r in range(rows - 1):
        row = input[r][start:end]
        current = ""

        for ch in row:
            if ch.isdigit():
                current += ch
            else:
                if current:
                    numbers.append(int(current))
                    current = ""
        
        if current:
            numbers.append(int(current))

    if op == "+":
        val = sum(numbers)
    else:
        val = 1
        for n in numbers:
            val *= n

    solution += val

print(f"day 5 part 1: {solution}")