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

    for col in range(end - 1, start - 1, -1):
        digits = []

        for row in range(0, rows - 1):  
            ch = input[row][col]

            if ch.isdigit():
                digits.append(ch)

        if digits:
            numbers.append(int("".join(digits)))

    print(numbers, op)

    if op == "+":
        val = sum(numbers)
        print(val)
    else:
        val = 1
        for n in numbers:
            val *= n
        print(val)

    solution += val

print(f"day 6 part 2: {solution}")