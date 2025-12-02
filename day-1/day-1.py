num1 = 50
num2 = 50
count1 = 0
count2 = 0

with open("day-1/input.txt") as f:
    input = f.read().splitlines()

for line in input:
    direction = line[0]
    steps = int(line[1:])

    sign = 1 if direction == 'R' else -1

    # part 1
    num1 = (num1 + (sign * steps)) % 100
    if num1 == 0:
        count1 += 1

    # part 2
    for _ in range(steps):
        num2 = (num2 + sign) % 100
    
        if num2 == 0:
            count2 += 1

print(f"part 1: {count1}")
print(f"part 2: {count2}")